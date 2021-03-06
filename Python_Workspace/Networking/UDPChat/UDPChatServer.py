# Import socket library
import socket as socket                                 

# Connection parameters
port = 8000                                                      # Port
server_ip = socket.gethostname()                                 # Server hostname (localhost)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)                         

# Bind the socket at given ip and port
sock.bind((server_ip, port))                   

# Continuously receive messages from clients and send messages to them accordingly
while True:
    recv_msg, client_addr = sock.recvfrom(1024)                  # Receive message and address from client
    print('Connected to: ', client_addr)
    print('Message received from client: ', recv_msg.decode())   # Convert message from byte to string
    msg_to_send = input('Enter message to send: ')
    sock.sendto(msg_to_send.encode(), client_addr)               # Send message to respective client

# Close the sockets
sock.close()
