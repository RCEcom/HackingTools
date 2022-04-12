import os
import time
import subprocess
def checksum(string, Ipv4):
    s1 = "[+]Ping..."
    for i in s1:
        print(i,end="")
        time.sleep(0.03)
    print()
    if(int(string) <= 255 and int(string) >= 248):
        s2 = "해당 IP에 대한 운영체제는 : Accel Linux, Linux, Cisco router, UNIX 4.0"
        for i in s2:
            print(i, end="")
            time.sleep(0.03)
        print()
    elif(int(string) <= 248 and int(string) >= 225):
         s2 = "해당 IP에 대한 운영체제는 :  Accel Linux, Linux, Cisco router,Unix 4.0, Solaris 2.x,Redhat Linux, Unix 4.0,Irix & Linux"
         for i in s2:
            print(i, end="")
            time.sleep(0.03)
    elif(int(string) <= 225 and int(string) >= 218):
        s2 = "해당 IP에 대한 운영체제는 : Unix 4.0, Solaris 2.x, Redhat Linux, Unix 4.0, Irix & Linux"
        for i in s2:
            print(i, end="")
            time.sleep(0.03)
        print()
    elif(int(string) <= 128 and int(string) >= 98):
        s2 = "해당 IP에 대한 운영체제는 : window"
        for i in s2:
            print(i, end="")
            time.sleep(0.03)
        print()
    else:
        s2 = "해당 IP에 대한 운영체제는 : Unix"
        for i in s2:
            print(i, end="")
            time.sleep(0.03)
        print()
v = input()
test_Ipv4 = []
test_Ipv4.append(v)
#Ipv4 = input("IP address or domain : ")
start_ms = "[+]" + "Operating system finder hacking program by \"RCEcom\""
for i in start_ms:
    print(i,end="")
    time.sleep(0.0001)
print()
print("-"*50)
for Ipv4 in test_Ipv4:
    cmd = "ping %s" % Ipv4
    f = open('TTL_bodyt.txt','w')
    sysMsg = subprocess.getstatusoutput(cmd)
    f.write(sysMsg[1])
    f.close()

    f = open('TTL_bodyt.txt', 'r')
    lines = f.readlines()

    for line in lines:
        if "TTL" in line:
            result = line
            break
    #3자릿수
    try:
        print("<==================%s====================>" % Ipv4)
        ttl = result[-4] + result[-3] + result[-2]
        checksum(ttl, Ipv4)
    #2자릿수
    except ValueError:
        ttl = result[-3] + result[-2]
        checksum(ttl, Ipv4)
    except NameError:
        print("호스트를 찾을 수 없습니다. 이름을 확인하고 다시 시도하십시오.")
