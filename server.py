#Aluno: Douglas Gomes de Paula - Matricula: 11621BCC013

import socket                               

s = socket.socket()                        
host = socket.gethostname()                 
port = 12345                               
s.bind((host, port))                        

s.listen(5)                                 

while True:
   print('Esperando conexão.')
   c, addr = s.accept()                     
   print('Conectado')
   while True:
      print('Esperando mensagem')
      c.send('your_turn'.encode())
      data = c.recv(1024).decode()
      if data != 'SAIR': 
         print('Mensagem recebida: ', data)
         print('Digite resposta: ')
         mensagem = input()
         c.send(mensagem.encode())
         print('Resposta enviada.')
      else:
         print('Conexão encerrada.')
         c.close()                           
         break
   
                            