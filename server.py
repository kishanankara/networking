import socket
import logging
import time
import signal
import os

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('tcpserver')
logger.setLevel(10)

def calculate_and_send(integers):
    logger.info('Values in array: %s' %integers)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8100))
    s = sum(integers)
    logger.info('Value of sum: %s' %(s))
    sock.send(s.to_bytes(10, 'big'))
    sock.close()

try:
    logger.info('PID: %s' %os.getpid())
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    integers = []
    active_connections = []
    visited_connections = []
    while True:
        i = 0
        sock.listen(5)
        active_connections.append(sock.accept())
        logger.info('Connections to be served: %s' % [x[1] for x in active_connections])
        logger.info('Connections already server: %s' %[x[1] for x in visited_connections])
        for connection in active_connections:
            if connection not in visited_connections:
                integers = []
                visited_connections.append(connection)
                active_connections.remove(connection)
                #Process connection values
                while i < 2:
                    val=connection[0].recv(10)
                    integers.append(int.from_bytes(val, 'big'))
                    i+=1
                calculate_and_send(integers)
    sock.close()
except KeyboardInterrupt:
    timer = 3
    print("\n")
    while timer > 0:
        print('Shutting down server in %s'%timer,"\r",end="")
        timer-=1
        time.sleep(1)
