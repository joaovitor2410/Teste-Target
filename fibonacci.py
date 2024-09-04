#inicializando as variaveis
atual = 1
anterior = 0
proximo = 0

#entrada de dados do usuario
num = int(input("Digite um número e verifique se ele pertence a sequencia de fibonacci:"))

#analisando o numero digitado pelo usuario
while proximo <= num:
    if proximo == num:
        print("O número {} está presente na sequencia de fibonacci" .format(num))
        break
    else:
        proximo = atual + anterior
        anterior = atual
        atual = proximo

if proximo > num:
    print("O número {} não esta presente na sequencia de fibonacci" .format(num))





