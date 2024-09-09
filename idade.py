idade = int(input('Digite sua idade:')) # Esta função exibe a mensagem entre parênteses e espera que o usuário digite um valor. 
if idade >= 10 and idade < 20:
   print(' Você é adolecente') 
   # Esta linha verifica se a idade está entre 10 (inclusive) e 20 (exclusive). 
elif idade >= 20 and idade < 30: 
    print('Você é jovem') 
    # É uma forma de adicionar mais condições ao bloco de código if. 
elif idade >= 30 and idade <= 100: 
   print('Você é adulto') 
   # Outra verificação elif para checar se a idade está entre 30 e 100 (inclusive). 
elif idade < 10 and idade >=0:
   print('Você é criança')
else: 
   print('Valor não encontrado!') 
   # Captura qualquer valor que não se encaixe nas condições anteriores. 
