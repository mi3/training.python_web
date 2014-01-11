import socket
import sys


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    # TODO: Replace the following line with your code which will instantiate 
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    #sock = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    print >>log_buffer, 'connecting to {0} port {1}'.format(*server_address)
    # TODO: connect your socket to the server here.
    sock.connect(server_address)

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print >>log_buffer, 'sending "{0}"'.format(msg)
        # TODO: send your message to the server here.
        l_msg = len(msg)
        sock.sendall(msg)

        # TODO: the server should be sending you back your message as a series
        #       of 16-byte chunks.  You will want to log them as you receive 
        #       each one.  You will also need to check to make sure that 
        #       you have received the entire message you sent __before__ 
        #       closing the socket. 
        # 
        #       Make sure that you log each chunk you receive.  Use the print 
        #       statement below to do it. (The tests expect this log format)

# Approach - Using for loop        
#        i = 0
#        for i in range(((l_msg -1 )/16) + 1) :
#            chunk = ''
#            chunk = sock.recv(16)
#            print >>log_buffer, 'received "{0}"'.format(chunk)

        # Or Using a while loop, having a reference to message length we sent helps 
        # to terminate it when msg size is same or multiples of buffer size
        done = False
        resp_len = 0
        while not done :
            chunk = sock.recv(16)
            print >>log_buffer, 'received "{0}"'.format(chunk)
            resp_len += len(chunk)
            if resp_len == l_msg:
                done = True        
    finally:
        # TODO: after you break out of the loop receiving echoed chunks from 
        #       the server you will want to close your client socket.
        print >>log_buffer, 'closing socket'
        sock.close()        

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usg = '\nusage: python echo_client.py "this is my message"\n'
        print >>sys.stderr, usg
        sys.exit(1)
    
    msg = sys.argv[1]
    client(msg)
