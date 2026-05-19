usuario_correto = 'Caique'
senha_correta = '1234'

tentativas = 3

while tentativas > 0:
    
    print('\n === Sistema de Login ===')

    usuario = input('Digite Seu Nome de Usuario: ')
    senha = input('Digite Sua Senha: ')
    
    print(usuario)
    print(senha)

    if usuario == usuario_correto and senha == senha_correta:
      print(' \n Login Realizado com Sucesso! ')
      break
    
    else:
         print('Usuario ou Senha Incorreta! Tente Novamente...')
    print(f'Voce tem {tentativas - 1} Tentativas Restantes...')
    
   
    if tentativas == 1:
         print('\n Voce Exedeu o Número de Tentativas Permitidas ! Acesso Bloqueado!')
         tentativas = 0
    else:     tentativas -= 1
    
    
    
