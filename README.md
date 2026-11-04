# ◈ TCP PORT SCANNER

### Network Reconnaissance · Python Sockets · TCP/IP

Um projeto desenvolvido em Python para verificar a disponibilidade de portas TCP em um host, utilizando a biblioteca nativa `socket` para estabelecer conexões e analisar as respostas obtidas.

A ferramenta explora conceitos fundamentais de redes de computadores, comunicação TCP/IP e reconhecimento de serviços, permitindo compreender na prática como conexões são estabelecidas entre clientes e hosts remotos.

## ◈ FEATURES

- **TCP Port Scanning:** tentativa de conexão com portas TCP especificadas.
- **Socket Programming:** utilização da biblioteca nativa `socket` do Python.
- **Connection Analysis:** interpretação do resultado das tentativas de conexão.
- **Timeout Handling:** controle do tempo de espera para evitar conexões bloqueadas indefinidamente.
- **Network Reconnaissance:** identificação de portas acessíveis em um host autorizado.
- **Resource Management:** encerramento adequado dos sockets após as operações.

## ◈ HOW IT WORKS

A ferramenta utiliza o mecanismo de conexão TCP para verificar se uma porta aceita conexões a partir do ambiente de execução.

O processo consiste em:

1. Receber o endereço do host e as portas que serão verificadas.
2. Criar um socket TCP.
3. Tentar estabelecer uma conexão com o destino.
4. Interpretar o resultado da tentativa.
5. Encerrar a conexão e apresentar os resultados.

Uma conexão bem-sucedida indica que a porta está acessível naquele momento. Uma conexão recusada pode indicar que não há um serviço aceitando conexões naquela porta. Já um timeout pode indicar filtragem, perda de pacotes, indisponibilidade ou outras condições de rede.

**Importante:** uma porta acessível não significa necessariamente que o serviço seja vulnerável.

## ◈ TECHNOLOGIES

- Python
- `socket`
- TCP/IP
- Tratamento de exceções
- Timeout de conexão

## ◈ SECURITY & ETHICAL USE

Esta ferramenta foi desenvolvida para aprendizado de redes, diagnóstico técnico e reconhecimento autorizado.

Utilize-a somente em sistemas próprios, ambientes de laboratório ou hosts para os quais você tenha autorização explícita.

## ◈ PROJECT GOAL

O objetivo é compreender como o estabelecimento de conexões TCP funciona na prática, como portas respondem a tentativas de conexão e como a programação com sockets pode ser aplicada a ferramentas de análise de redes.

<p align="center">
  <strong>NETWORKING · PYTHON · TCP/IP</strong>
</p>













# ◈ HTTP CLIENT FROM SCRATCH

### HTTP Protocol · Raw Sockets · Python Networking

Um projeto desenvolvido em Python para explorar a comunicação HTTP utilizando sockets, construindo e enviando requisições diretamente pela camada de transporte, sem depender de bibliotecas de alto nível como `requests`.

A proposta é compreender o funcionamento interno da comunicação entre clientes e servidores web, observando como requisições são estruturadas, transmitidas e interpretadas por meio de conexões TCP.

## ◈ FEATURES

- **Socket-Based Communication:** estabelecimento de conexões TCP com servidores HTTP.
- **HTTP Request Construction:** montagem manual de requisições HTTP.
- **Request Headers:** definição de cabeçalhos como `Host`, `User-Agent` e `Connection`.
- **Response Analysis:** leitura e análise da resposta recebida do servidor.
- **Status Code Inspection:** identificação do código de status HTTP retornado.
- **Protocol Fundamentals:** estudo da relação entre HTTP e TCP.
- **Low-Level Networking:** comunicação direta por sockets, com maior controle sobre os dados transmitidos.

## ◈ HOW IT WORKS

O projeto reproduz as etapas fundamentais de uma comunicação HTTP sobre TCP:

1. Resolver o host e identificar o endereço de destino.
2. Estabelecer uma conexão TCP com a porta apropriada.
3. Construir a requisição HTTP com a linha inicial, os cabeçalhos e os separadores exigidos pelo protocolo.
4. Enviar os dados pelo socket.
5. Receber e interpretar os bytes retornados pelo servidor.
6. Encerrar a conexão e analisar a resposta.

Esse processo permite observar como métodos HTTP, cabeçalhos, códigos de status e corpos de resposta participam da comunicação entre aplicações web.

## ◈ PROTOCOL KNOWLEDGE

O projeto oferece uma base prática para estudar:

- Métodos HTTP, como `GET` e `HEAD`.
- Cabeçalhos de requisição e resposta.
- Códigos de status HTTP.
- Resolução de nomes e conexões TCP.
- Delimitação de mensagens e leitura de dados recebidos.
- Diferenças entre comunicação HTTP e HTTPS.

**Nota técnica:** HTTP sobre TCP não oferece criptografia por si só. Para HTTPS, é necessário estabelecer TLS corretamente antes de transmitir a comunicação HTTP. A implementação de um cliente HTTP básico também precisa considerar respostas fragmentadas, encerramento da conexão e diferentes formas de delimitação do corpo.

## ◈ TECHNOLOGIES

- Python
- `socket`
- `struct` e tratamento de bytes, quando necessários
- HTTP
- TCP/IP
- DNS

## ◈ SECURITY & WEB ANALYSIS

Entender o protocolo HTTP em baixo nível é útil para estudar o comportamento de aplicações web, investigar requisições e respostas e desenvolver uma compreensão mais sólida das superfícies de comunicação de sistemas.

O projeto constitui uma base educacional para aprofundar conhecimentos em análise de tráfego, segurança de aplicações web e funcionamento de APIs.

## ◈ PROJECT GOAL

O objetivo é compreender o que acontece por trás de uma requisição web, desde a abertura do socket até a recepção dos dados enviados pelo servidor, reduzindo a dependência de abstrações de alto nível e fortalecendo os fundamentos de redes e protocolos.

<p align="center">
  <strong>PYTHON · SOCKETS · HTTP · WEB SECURITY</strong>
</p>
