import socket

SERVER_PORT = 8888

def connect_to_server():
  clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  clientSocket.connect(('192.168.213.128', SERVER_PORT))

# Receive the quote from the server
quote = clientSocket.recv(1024).decode()
print("Received Quote of the Day:",quote)

clientSocket.close()

if __name__ == "__main__":
  connect_to_server()
