from socket import *
from time import ctime
import getIp

ctrCmd = [b"Open", b"Stop", b"Close", b"Num"]

messageBack = ["Pool opens", "Pool stops", "Pool closes", "2"]

HOST = '192.168.0.192'
PORT = 13000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print ("Waiting for connection")
    tcpCliSock, addr = tcpSerSock.accept()
    hostName = getIp.getHostIp(addr)
    print ("...connected from: ", hostName, addr)
    try:
        while True:
            data = ""
            data = tcpCliSock.recv(BUFSIZE)
            if not data:
                break
            if data == ctrCmd[0]:
                message_to_send = messageBack[0].encode("UTF-8")
                tcpCliSock.send(len(message_to_send).to_bytes(2, byteorder='big'))
                tcpCliSock.send(message_to_send)
            if data == ctrCmd[1]:
                message_to_send = messageBack[1].encode("UTF-8")
                tcpCliSock.send(len(message_to_send).to_bytes(2, byteorder='big'))
                tcpCliSock.send(message_to_send)
            if data == ctrCmd[2]:
                message_to_send = messageBack[2].encode("UTF-8")
                tcpCliSock.send(len(message_to_send).to_bytes(2, byteorder='big'))
                tcpCliSock.send(message_to_send)
            if data == ctrCmd[3]:
                message_to_send = messageBack[3].encode("UTF-8")
                tcpCliSock.send(len(message_to_send).to_bytes(2, byteorder='big'))
                tcpCliSock.send(message_to_send)
    except KeyboardInterrupt:
        print("...Interrupt")
        #test.close()
        #GPIO.cleanup()

tcpSerSock.close()