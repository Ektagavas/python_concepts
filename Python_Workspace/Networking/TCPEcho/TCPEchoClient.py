# Import socket library
import socket as socket                                 

# Connection parameters
port = 8000                                             # Port
server_ip = socket.gethostname()                        # Server hostname (localhost)

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

# Connect to server socket
client_socket.connect((server_ip, port))

# Continuously send messages to server and receive the same messages back
while True:
    msg = input('Enter message: ')
    client_socket.send(msg.encode())                    # Convert message from bytes to string
    recv_msg = client_socket.recv(port).decode()        # Convert message from bytes to string 
    if not recv_msg: break
    print('Message received from server: ', recv_msg)

# Close the socket
client_socket.close
