
import time
import socket
import websockets

ClientSocket = socket.socket()
class Messenger:
    def send_message(self,message,server):
        server.send_message(message)
        print(f"Sent message '{message}' to server'{server.name}'")

    def send_messages_sequentially(self,messages,servers):

        for server in servers:
            ClientSocket.connect((server))
            ClientSocket.send(messages)

class WebSocketServer:
    def __init__(self,name):
        self.name = name

    def send_message(self,message):
        # simulate some delay before sending the message
        import time
        time.sleep(10)
        print(f"recieved message'{message} on server '{self.name}'")

def main():
    messages = 'relay'
    server1 = WebSocketServer('192.168.0.145:9202')
    server2 = WebSocketServer('192.168.0.145:9203')
    server = [server1,server2]
    messenger = Messenger()

    messenger.send_messages_sequentially(messages,server)

main()