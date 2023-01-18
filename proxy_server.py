import socket
import multiprocessing as mp

def proxy_server(conn, addr, clnt, ):
	print("Client from address: ", addr)
	conn.settimeout(0.5)
	try:
		buff = conn.recv(4086)
		while(True):
			buff += conn.recv(4086)
	except TimeoutError:
		pass
	except Exception:
		print("\t Unable to read")
		conn.close()
		clnt.close()
		exit()
	print(addr, "sending")
	clnt.sendall(buff)

	try:
		print(addr, "reciving from client")
		buff = clnt.recv(4086)
		while(True):
			buff += clnt.recv(4086)
	except TimeoutError:
		pass
	except Exception:
		print("\t Unable to send to client")
		conn.close()
		exit()
	print(addr, "sendall")
	conn.sendall(buff)

	conn.close()

def main():
	google = socket.gethostbyname("www.google.com")
	google_port = 80
	localhost = "127.0.0.1"
	port = 8001

	try:
		clnt = socket.create_connection((google, google_port), )
	except Exception as e:
		print("\tUnable to connect to google: ", str(e))
		conn.close()
		exit()
	clnt.settimeout(0.5)
	try:
		server = socket.create_server((localhost, port), backlog=200, reuse_port=True)
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	except Exception as e:
		print("\tUnable to create a server: ", str(e))
		exit()
	
	while(True):
		conn, addr = server.accept()
		p = mp.Process(target=proxy_server, args=(conn, addr, clnt, ))
		p.start()

if __name__ == "__main__":
	main()
