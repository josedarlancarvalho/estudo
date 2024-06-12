#operadores logicos

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
#no and os dois tem que ser true para a resposta dar true
#no or apenas um precisa ser true para a resposta dar true

saldo = 1000
saque = 200
limite = 100
conta_especial = True


x= saldo >= saque and saque <= limite
print (x)

#para ser verdadeiro ele precisa que as duas operacoes sejam verdadeiras



x= saldo >= saque or saque <= limite
print (x)

#para ser verdadeiro ele precisa que apenas uma operacao seja verdadeira



x= not 100 > 50
print(x)

#ele é a negacao, ou seja, ele vai dar o contrario da respostas. se for verdadeiro ele da falso e se for falso ele dar verdadeiro



saldo >= saque and saque <= limite or conta_especial and saldo >= limite
#resposta >>> True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= limite)
#resposta >>> True
#o parenteses() é bom para deixar o codigo mais organizado, ate pq na expressao acima ele ta comparando um com outro, da pra notar isso pelo or, ou seja, fica bem melhor para ve e entender.



