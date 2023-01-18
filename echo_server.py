import socket
import multiprocessing as mp

def handle_client(conn, addr):
	print("Connected to: ", addr)
	try:
		buff = conn.recv(4086)
		print(buff)
		conn.send(buff)
	except Exception as e:
		print(str(e))
	conn.close()

def main():
	localhost = "127.0.0.1"
	port = 8001

	ser = socket.create_server((localhost, port), backlog=200)

	while(True):
		try:
			conn, addr = ser.accept();
			p = mp.Process(target=handle_client, args=(conn, addr, ))
			p.start()
		except:
			print(str(error))
			continue
			
if(__name__ == "__main__"):
	main()
