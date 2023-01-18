import socket
import time 
host = "127.0.0.1"
port = 8001
request = b"GET / HTTP/1.1\n\n"

try:
	s = socket.create_connection((host, port))
except Exception as e:
	print("Unable to connect: ", str(e))
	exit()
s.sendall(request)

time.sleep(1.0)

s.settimeout(1.0)
total_buff = b""
try:
	while(True):
		buff = s.recv(4096)
		total_buff += buff
		if(not buff or len(buff) < 4096):
			break
except TimeoutError:
	pass
print(total_buff)
