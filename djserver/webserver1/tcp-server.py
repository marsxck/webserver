import sys
import time
import gevent
from gevent import socket,monkey
import demjson
monkey.patch_all()
def handle_request(conn):
    while True:
        data=conn.recv(1024)
        if not data:
            conn.close()
            break
        a=data.decode('utf-8')
        b=demjson.decode(a)
        with open("learn/templates/histroy1","a+") as f1:
            f1.write(a)
            f1.write(time.strftime('%Y-%m-%d-%H:%M',time.localtime(time.time())))
            f1.write('\n')
        with open("learn/templates/src","w+") as f1:
            f1.write(b["src"])
        with open("learn/templates/sr","w+") as f1:
            f1.write(b["sr"])
        #with open("/var/www/html/src","wb+") as f:
       # f=open('/var/www/html/src','wb+')
            #f.write(data)
        #f.close()
def server(port):
    s=socket.socket()
    s.bind(('172.21.16.2',port))
    s.listen(5)
    while True:
        cli,addr=s.accept()
        gevent.spawn(handle_request,cli)
if __name__=='__main__':
    server(7788)
