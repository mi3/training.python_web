import socket
import sys
import mimetypes
import os

def response_ok( body=None, mimetype=None):
    """returns a basic HTTP response"""
    mime_type = "Content-Type: "
    resp = []
    resp.append("HTTP/1.1 200 OK")
    mime_type+=mimetype
    resp.append(mime_type)
    resp.append("")
    resp.append(body)
    return "\r\n".join(resp)


def response_method_not_allowed():
    """returns a 405 Method Not Allowed response"""
    resp = []
    resp.append("HTTP/1.1 405 Method Not Allowed")
    resp.append("Content-Type: text/plain")
    resp.append("")
    resp.append("Error 405: Method not allowed")
    return "\r\n".join(resp)


def parse_request(request):
    first_line = request.split("\r\n", 1)[0]
    method, uri, protocol = first_line.split()
    if method != "GET":
            raise NotImplementedError("We only accept GET")
    print >>sys.stderr, 'request is okay'
    return uri

def response_not_found():
    """returns a 404 Resource not found response"""
    resp = [] 
    resp.append("HTTP/1.1 404 Not Found\n")
    resp.append("")
    resp.append("Error 404: File not found")
    return "\r\n".join(resp)

def resolve_uri(a_uri):
    mime = ""
    resp = ""
    r_dir = "./webroot"
    
    if(a_uri == '/'):
        resource = r_dir
    resource = r_dir + a_uri

    if( os.path.isfile(resource) or os.path.isdir(resource) ):    
    
        if os.path.isfile(resource):
            #is a file
            mtype = mimetypes.guess_type(resource)[0]
            if mtype == 'text/plain':
                fd = open(resource,'r')
            else :
                fd = open(resource,'rb')
            resp = fd.read()
            fd.close()
           
        if os.path.isdir(resource):
            #is a dir 
            mtype = 'text/html'
            print resource 
            for filename in os.listdir(resource):
                resp+="<a href=%s> %s </a> <br>" \
                    %(resource.split('/')[-1]+"/"+filename,filename)
                
    else :
        raise ValueError("Resource not found")
    return  resp, mtype

    

def server():
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print >>sys.stderr, "making a server on %s:%s" % address
    sock.bind(address)
    sock.listen(1)
    
    try:
        while True:
            print >>sys.stderr, 'waiting for a connection'
            conn, addr = sock.accept() # blocking
            try:
                print >>sys.stderr, 'connection - %s:%s' % addr
                request = ""
                while True:
                    data = conn.recv(1024)
                    request += data
                    if len(data) < 1024 or not data:
                        break

                try:
                    print >>sys.stderr, request
                    if not request:
                        print "EMPTY Request\n"
                        continue
                    r_uri = parse_request(request)
                except NotImplementedError:
                    response = response_method_not_allowed()
                else:            
                    try:    
                        re, mi = resolve_uri(r_uri)
                    except ValueError:
                        response = response_not_found()
                    else:
                        response = response_ok(re, mi)

                print >>sys.stderr, 'sending response'
                conn.sendall(response)
            finally:
                conn.close()
            
    except KeyboardInterrupt:
        sock.close()
        return


if __name__ == '__main__':
    server()
    sys.exit(0)
