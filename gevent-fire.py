## Author - Mohit. ((  Git -: http://github.com/mohi048  ))
## Python script to fire telnet requests on local server/localhost on specific port using gevent threads
## usage python gevent-fire.py 9000 200
## This would send 200 telnet requests on port 9000 of your local server

from gevent.pool import Pool
from telnetlib import Telnet
#from gevent import monkey
#monkey.patch_all()
import sys
import datetime

def worker(url):
    tn = Telnet(url,port)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "\n Usage - python gevent-fire.py dst_port num_of_requests"
    else:
	port = int(sys.argv[1])
	requests = int(sys.argv[2])
	url = ['0.0.0.0'] * requests
        pool = Pool(20)
	startTime = datetime.datetime.now()
	pool.map(worker, url)
	print "*"*60
	print " Total Time to execute ",datetime.datetime.now() - startTime
	print "*"*60