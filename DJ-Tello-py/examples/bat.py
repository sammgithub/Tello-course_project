import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(b'command', 0, ('192.168.10.1', 8889))
sock.sendto(b'battery?', 0, ('192.168.10.1', 8889))

while True:
	data, ip = sock.recvfrom(1024)
print("{}: {}".format(ip, data.decode()))