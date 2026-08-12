import socket

print('bem vindo ao destwarrio scan')
alvo=input('defina o ip alvo :')
portas= 22
s=socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
    

)
resultado = s.connect_ex((alvo, portas))

s.close()

print(resultado)