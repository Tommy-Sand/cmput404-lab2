import socket

host = socket.gethostbyname("www.google.com")
port = 80

try:
	sock = socket.create_connection((host, port))
except:
	print("Unable to connect")
	exit()

try:
	sock.settimeout(1.0)
	sock.send("GET / HTTP/1.1\n\n".encode("utf-8"))
	buff = sock.recv(4086)
	while(True):
		buff += sock.recv(4086)

except TypeError as type_error:
	print(str(error))
	sock.close()
except TimeoutError as to_error:
	print(buff)
	sock.close()

