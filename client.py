import socket

def send_student_id_to_server(student_id, host, port):
    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((host, port))

        # Send student ID to the server
        client_socket.sendall(student_id.encode())

        # Receive and print the server response
        response = client_socket.recv(1024)
        print("Server Response:", response.decode())

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    # Replace 'YOUR_STUDENT_ID' with your actual UiTM Student ID
    student_id = "2021871656"
    server_host = "izani.synology.me"
    server_port = 8443

    send_student_id_to_server(student_id, server_host, server_port)
