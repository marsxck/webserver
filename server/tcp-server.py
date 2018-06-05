import sys
import time
import gevent
from gevent import socket,monkey
monkey.patch_all()
def handle_request(conn):
    while True:
        data=conn.recv(1024)
        if not data:
            conn.close()
            break
        f=open('/var/www/html/src2','wb+')
        f.write(data)
        f.close()
def server(port):
    s=socket.socket()
    s.bind(('172.21.16.2',port))
    s.listen(5)
    while True:
        cli,addr=s.accept()
        gevent.spawn(handle_request,cli)
if __name__=='__main__':
    server(7788)
