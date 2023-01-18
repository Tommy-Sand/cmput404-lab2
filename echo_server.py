import socket

localhost = "127.0.0.1"
port = 8001

try:
	ser = socket.create_server((localhost, port), backlog=200)
except Exception as e:
	print(str(e))

while(True):
	try:
		conn_soc, clt_addr = ser.accept();
	except:
		print(str(error))
		continue

	try:
		buff = conn_soc.recv(4086)
		print(buff)
		conn_soc.send(buff)
	except Exception as error:
		print(str(error))
	conn_soc.close()	
