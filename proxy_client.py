import socket

host = "127.0.0.1"
port = 8001
request = b"GET / HTTP/1.1\n\n"

try:
	s = socket.create_connection((host, port))
except:
	print("unable to connect")
	exit()

s.sendall(request)
s.settimeout(5.0)
try:
	while(True):
		buff = s.recv(4086)
		print(buff)
except TimeoutError as to_error:
	print("Timed out" )
	s.close()
except Exception as e:
	print("Error while reading")
	print(str(e))
	s.close()

