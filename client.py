import socket

HOST = '127.0.0.1'
PORT = 1994
# Create Socket(Use TCP)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Make A Socket Connection
client.connect((HOST, PORT))
cmd = input("Please Input Msg:")
client.send(cmd.encode('utf-8'))
data = client.recv(1024)
print(data.decode('utf-8'))