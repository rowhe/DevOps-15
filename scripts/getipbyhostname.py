#!/usr/bin/env python3
import time
import socket
host1 = "drive.google.com"
host2 = "mail.google.com"
host3 = "google.com"

hosts = {host1: socket.gethostbyname(host1), host2: socket.gethostbyname(host2), host3: socket.gethostbyname(host3)}

while 1 == 1:
    for i in hosts:
        ip = socket.gethostbyname(hosts[i])
        if hosts[i] == ip:
            print(i, ip)
        else:
            print("[ERROR]", i, "IP mismatch:", "old ip:", hosts[i], "new ip", ip)
            exit(1)
    time.sleep(50)
