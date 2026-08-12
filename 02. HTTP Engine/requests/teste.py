import socket

porta=int(input("digite sua porta: "))

host=input("digite seu host:")

ip=socket.gethostbyname(host)


r=socket.socket(

    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
)

cn=r.connect_ex((ip, porta))

print(cn)