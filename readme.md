# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"

## Обязательные задания

1. Мы выгрузили JSON, который получили через API запрос к нашему сервису:
	```json
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
	```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

* Исправленный вывод будет выглядеть примерно так:
```json
{
  "info": "Sample JSON output from our service",
  "elements": [
    {
      "name": "first",
      "type": "server",
      "ip": "71.75.22.43"
    },
    {
      "name": "second",
      "type": "proxy",
      "ip": "71.78.22.43"
    }
  ]
}
```

2. В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.
* Вариант такого скрипта:
```python
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
```
* Вывод такого скрипта выглядит следующим образом:
```bash
vagrant@netology1:~/git/DevOps-15/scripts$ nano 5.py
vagrant@netology1:~/git/DevOps-15/scripts$ ./5.py
drive.google.com 142.251.1.194
[ERROR] ['mail.google.com'] IP mismatch: old ip: ['108.177.14.83'] new ip 108.177.14.19
[ERROR] ['google.com'] IP mismatch: old ip: ['74.125.131.138'] new ip 74.125.131.101
!!!updating .json
!!!updating .yml
drive.google.com 142.251.1.194
[ERROR] ['mail.google.com'] IP mismatch: old ip: ['108.177.14.19'] new ip 108.177.14.17
[ERROR] ['google.com'] IP mismatch: old ip: ['74.125.131.101'] new ip 74.125.131.113
!!!updating .json
!!!updating .yml
drive.google.com 142.251.1.194
[ERROR] ['mail.google.com'] IP mismatch: old ip: ['108.177.14.17'] new ip 108.177.14.18
[ERROR] ['google.com'] IP mismatch: old ip: ['74.125.131.113'] new ip 74.125.131.139
```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

---