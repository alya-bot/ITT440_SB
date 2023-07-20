import socket
import threading
import random

# List of quotes
quotes = [
    "Be yourself; everyone else is already taken. ",
    "Be the change that you wish to see in the world.",
    "The only way to do great work is to love what you do.",
    "You only live once, but if you do it right, once is enough.",
    "The best way to predict the future is to invent it. ",
    "La Tahzan Innallaha Ma’ana"
]

def handle_client(client_socket):
    # Send a random quote to the client
    random_quote = random.choice(quotes)
    client_socket.send(random_quote.encode())
    client_socket.close()

def main():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind(('', 8888))

    # Start listening for incoming connections
    server_socket.listen(5)
    print("Server listening on port 8888...")

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    main()

