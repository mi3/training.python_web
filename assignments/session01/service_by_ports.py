#!/usr/bin/python

import socket 
import sys

def fetch_serv(l_range = 0, u_range = 10):
    for i in range(l_range, u_range+1):    
        try:   
            serv = socket.getservbyport(i) 
        except socket.error, msg:
            serv = msg

        print i, serv


if __name__ == '__main__':

    if len(sys.argv) == 1 and sys.argv[0] == "service_by_ports.py":
        fetch_serv()
        sys.exit(1)
    elif len(sys.argv) != 3:
        usg = '\nusage: service_by_ports.py <lower bound> <upper bound>\n'
        print >>sys.stderr, usg 
        sys.exit(1)
    
    l_range = int(sys.argv[1])
    u_range = int(sys.argv[2])
   
    if((l_range > 0 and l_range < 65536) and (u_range > 0 and u_range < 65536) and (u_range > l_range)):
        fetch_serv(l_range, u_range)
    else:
        print "Port range is 0-65535"    
