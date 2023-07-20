import socket

SERVER_PORT 8888

def bar_to_atmosphere(pressure):
    return pressure * 0.986923

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', SERVER_PORT))
    server_socket.listen(1)
  
    print(f"Server is listening on {SERVER_PORT}...")
  
    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established from {addr}")
      
        try:
            data = conn.recv(1024)
            if not data:
                break
              
            bar_pressure = float(data.decode())
            atmosphere_pressure = bar_to_atmosphere(bar_pressure)

            conn.send(str(atmosphere_pressure).encode())
          
        except ValueError:
            conn.send(b"Invalid input")
          
        finally:
            conn.close()

if __name__ == "__main__":
    main()
