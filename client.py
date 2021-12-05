#Aluno: Douglas Gomes de Paula - Matricula: 11621BCC013

import socket                               

s = socket.socket()                         
host = socket.gethostname()                
port = 12345                               

print('Conectando-se ao servidor')
s.connect((host, port))
print('Conectado')

while True: 
    data = s.recv(1024).decode()
    if data == 'your_turn':            

        print('Digite mensagem: ')
        mensagem = input()

        if mensagem != 'SAIR':
            s.send(mensagem.encode())
            print('Mensagem enviada')
            print('Esperando resposta')
        else: 
            print('Desconectando.')
            s.send(mensagem.encode())
            break
    else: 
        print('Resposta recebida: ', data)
