import socket

porta=80

# entrada de dados inicias e converçao de host e caminho no mesmo modelo 
entrada=input("digite seu host:")

processo=entrada.split("/", 1)[0]

caminho=entrada
host=processo

ip=socket.gethostbyname(host)


# parte da conexao 
r=socket.socket(

    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
)

cn=r.connect_ex((ip, porta))

#modelo get requisiçao para o site 
p=f"GET /{caminho} HTTP/1.1\r\nHost:{host}\r\n\r\n"
codificado=p.encode()

r.sendall(codificado)
resposta=r.recv(4096)
resposta=resposta.decode()
print(resposta)



