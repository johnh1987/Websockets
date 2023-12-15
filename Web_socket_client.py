import socket
import time

host = '192.168.0.94'
port = 9000

ClientSocket = socket.socket()
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
Response = ClientSocket.recv(2048)

count = 0


while True:
    count1 = count - 1
    count2 = count - 2
    count3 = count - 3
    count4 = count - 4
    count5 = count - 5
    count6 = count - 6
    count7 = count - 7
    count8 = count - 8
    count9 = count - 9

    Input = ("A",count,count1,count2,count3,count4,count5,count6,count7,count8,count9)
    Input = str(Input)
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(2048)
    #print(Response.decode('utf-8'))
    count +=1
    time.sleep(1)
ClientSocket.close()