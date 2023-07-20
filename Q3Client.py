import socket

SERVER_PORT 8888

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.213.128', SERVER_PORT))
  
    try:
        user_input = input("Enter pressure value in bar: ")
        client_socket.send(user_input.encode())

        atmosphere_pressure = client_socket.recv(1024).decode()
        print(f"Received atmosphere-standard pressure: {atmosphere_pressure} atm")
      
    except ValueError:
        print("Invalid input")
      
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
