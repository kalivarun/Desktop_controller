import socket
import threading



print('''

 <!>BASIC INSTRUCTIONS

-> This server has the ablity to connect
   more then 5 devices under LAN router

-> Make sure that port number 5000
   is free before running the program

-> Make sure to convert the
   client.py to client.exe using pyinstaller
   > client.exe program should run in target pc 

-> Remote_10.py is a app based prorgam
   install pydroid 3 in your mobile
   >make sure to run the Remote_10 under
    same router as target pc 

''')
# Function to handle a single client
def handle_client(client_socket):
    # Receive data from the client
    request = client_socket.recv(1024)
    print(f"Received data: {request.decode('utf-8')}")

    # Send a response to the client
    response = "Hello from the server!"
    client_socket.send(response.encode('utf-8'))

    # Close the client socket
    client_socket.close()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('0.0.0.0', 5000))

# Enable the server to accept connections
server_socket.listen(5)
print("Server listening on port 5000...")

while True:
    # Wait for a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
