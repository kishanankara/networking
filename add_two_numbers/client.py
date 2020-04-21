import socket
import argparse
import sys
import logging
import time

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('tcpclient')
logger.setLevel(10)
def start_server(integers):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('localhost', 8000))
    sock.send(int(integers[0]).to_bytes(10, 'big'))
    sock.send(int(integers[1]).to_bytes(10, 'big'))
    sock.close()
    def recv_server():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 8100))
        sock.listen(1)
        clisockm, address = sock.accept()
        val = clisockm.recv(10)
        print(int.from_bytes(val, 'big'))
        sock.close()
    recv_server()
if len(sys.argv) < 2:
    logger.error('Sufficient arguments not provided. Please provide two integers.')
else:
    start_server([sys.argv[1], sys.argv[2]])
timer = 3
while timer > 0:
    print('Exiting the server in %s'%timer,"\r",end="")
    timer-=1
    time.sleep(1)
