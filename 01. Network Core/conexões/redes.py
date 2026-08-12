import socket

host = input("digite seu host: ")
ip = socket.gethostbyname(host)

portas = [
    80,
    443,
    22,
    8080,
    8443,
    8000,
    8081,
    8082,
    8008,
    8888,
    3000,
    5000,
    8083,
    8084,
    8085,
    8086
]

abertas = []
fechadas = []

for porta in portas:

    r = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM
    )

    r.settimeout(0.3)

    resultado = r.connect_ex((ip, porta))

    if resultado == 0:
        abertas.append(porta)
    else:
        fechadas.append(porta)

    r.close()

print("Portas abertas:", abertas)
print("Portas fechadas:", fechadas)