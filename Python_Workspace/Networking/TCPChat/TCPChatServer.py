# Import socket library
import socket as socket                                 

# Connection parameters
port = 8000                                             # Port
server_ip = socket.gethostname()                        # Server hostname (localhost)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)                         

# Bind the socket at given ip and port
server_socket.bind((server_ip, port))                   

# Listen to incoming request
server_socket.listen(1)                                

# Accept connection from client
client_socket, client_addr = server_socket.accept()     
print('Connected to ', client_addr)

# Continuously receive the message from client and echo back
while True:
    recv_msg = client_socket.recv(port).decode()             # Convert message from bytes to string
    if not recv_msg: break
    print('Message received from client: ', recv_msg)
    msg_to_send = input('Enter message to send: ')
    client_socket.send(msg_to_send.encode())                    # Convert message from string to bytes

# Close the sockets
client_socket.close                                     
server_socket.close
