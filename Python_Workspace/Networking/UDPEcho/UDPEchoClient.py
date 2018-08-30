# Import socket library
import socket as socket                                 

# Connection parameters
port = 8000                                                     # Port
server_ip = socket.gethostname()                                # Server hostname (localhost)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)  

# Continuously send messages to server and receive back the same
while True:
    msg = input('Enter message to send: ')
    sock.sendto(msg.encode(), (server_ip, port))                # Send message in bytes to server
    message, addr = sock.recvfrom(1024)                         # Receive the message from server
    print('Message received from server: ', message.decode())

# Close the socket
sock.close()