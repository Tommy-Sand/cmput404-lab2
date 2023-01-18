import socket
import multiprocessing as mp
import time

def proxy_server(conn, addr):
	google = socket.gethostbyname("www.google.com")
	google_port = 80

	print("Client from address: ", addr)
	try:
		clnt = socket.create_connection((google, google_port), )
	except Exception as e:
		print("\tUnable to connect to google: ", str(e))
		conn.close()
		exit()
	
	total_buff = b""
	conn.settimeout(0.5)
	clnt.settimeout(0.5)
	try:
		while(True):
			buff = conn.recv(4096)
			total_buff += buff
			if(not buff):
				break
	except TimeoutError as to_error:
		pass
	print(total_buff)
	print(addr, "sending")
	clnt.sendall(buff)

	time.sleep(0.5)

	total_buff = b""
	print(addr, "reciving from client")
	try:
		while(True):
			buff = clnt.recv(4096)
			total_buff += buff
			if(not buff):
				break
	except TimeoutError as to_error:
		pass
	print(addr, "sendall")
	conn.sendall(total_buff)
	clnt.close()
	conn.close()

def main():
	localhost = "127.0.0.1"
	port = 8001

	
	try:
		server = socket.create_server((localhost, port), backlog=200, reuse_port=True)
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	except Exception as e:
		print("\tUnable to create a server: ", str(e))
		exit()
	
	while(True):
		conn, addr = server.accept()
		p = mp.Process(target=proxy_server, args=(conn, addr, ))
		p.start()

if __name__ == "__main__":
	main()
