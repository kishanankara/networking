import socket
import logging
import time

#TODO Make the server running forever and accepting connections.

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('tcpserver')
logger.setLevel(10)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('localhost', 8000))
integers = []
while True:
    i = 0
    sock.listen(5)
    clisockm, address = sock.accept()
    while i < 2:
        val=clisockm.recv(10)
        integers.append(int.from_bytes(val, 'big'))
        i+=1
        sock.close()
    break
logger.info('Values in array: %s' %integers)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8100))
s = sum(integers)
logger.info('Value of sum: %s' %(s))
sock.send(s.to_bytes(10, 'big'))
sock.close()
timer = 3
while timer > 0:
    print('Exiting the server in %s'%timer,"\r",end="")
    timer-=1
    time.sleep(1)
