
fatorial = 1  # iniciaremos a variável com o valor 1, pois com ela será realizado e armazenado o valor do fatorial
cont = 1  # iniciaremos a variável com o valor 1, pois será ultilizada para o calculo e para controlar o loop

"""
No bloco de código abaixo será realizado o calculo do fatorial de 100;
Para isso, foi usado uma variável 'cont' que irá servir para incrementar o valor que será 
multiplicado ao fatorial, e também para contar o loop .
"""

while cont <= 100:
    fatorial = fatorial * cont
    cont += 1

print(fatorial)  # mostrará o fatorial de 100

soma = 0  # varivel que sevira para somar cada número do fatorial de 100.
while fatorial > 0:  # vai percorrer todos os números do fatorial de 100.
    soma += fatorial % 10  # aqui o programa vai pegar o ultimo número e somar na variavel soma.
    fatorial = fatorial // 10  # vai pegando os números a serem somados de trás para frente.

print('Resultado da soma dos números do fatorial de 100: ', soma)  # printa o resultado final

