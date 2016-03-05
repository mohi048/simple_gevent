## Author - Mohit. ((  Git -: http://github.com/mohi048  ))
## Python script to listen the requests on localhost specific port using gevent threads
## usage python gevent-listner.py 9000 
## This would listen on port 9000 of your local server


import gevent
import datetime
import sys

def handle_request(x,y):
    print '='*20
    print "Listening on port {0}".format(port)
    print "Recieved connection #: {0}".format(next(x))
    print str(datetime.datetime.now())

def create_counter():
    n = 1
    while True:
        yield n
        n += 1

def greenlet(port):
    from gevent import socket
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    print "Listner started at port # {0}".format(port)
    s.listen(500)
    c = create_counter()
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, c, gevent.sleep)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "\n Usage - python gevent-socket.py port_number"
    else:
        port = int(sys.argv[1])
        greenlet(port)
