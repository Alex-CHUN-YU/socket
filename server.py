import socket

HOST = '127.0.0.1' # Server IP(Change to your IP)
PORT = 1994
# Create Socket(Use TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
# Start Listen(Max Count = 5)
server.listen(5)

print('Server Start At: %s:%s' %(HOST, PORT))
print('Wait For Connection...')

while True:
    conn, addr = server.accept()
    print ("Got Connection From", addr)
    message = conn.recv(1024).decode('utf-8')
    print(message)
    conn.send(("Server Receive Your Messages Is '" + message + "'").encode('utf-8'))