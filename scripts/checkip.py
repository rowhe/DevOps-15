#!/usr/bin/env python3
import time
import socket
import os
import json
import yaml

host1 = "drive.google.com"
host2 = "mail.google.com"
host3 = "google.com"

hosts = [{host1: socket.gethostbyname(host1)}, {host2: socket.gethostbyname(host2)}, {host3: socket.gethostbyname(host3)}]

while True:
  os.system("systemd-resolve --flush-caches")
  for names in hosts:
    for i in names.keys():
      ip = socket.gethostbyname(i)
    if names[i] == ip:
      print(i, ip)
    else:
      print("[ERROR]", list(names.keys()), "IP mismatch:", "old ip:", list(names.values()) , "new ip", ip)
      names[i]=ip
    time.sleep(1)


  with open("hosts.json", "w") as file1:
    file1.write(json.dumps(hosts, indent=2))
  print("!!!updating .json")
  with open("hosts.yaml", "w", encoding="utf-8") as file2:
    file2.write(yaml.dump(hosts))
  print("!!!updating .yml")
