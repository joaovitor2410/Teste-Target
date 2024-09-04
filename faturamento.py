#importando a biblioteca json
import json

#atribuindo os dados a uma variavel
with open('dados.json') as f:
    dados = json.load(f)

#analisando os valores de faturamento
faturamento = [item['valor'] for item in dados]

#calculando o menor, o maior e a media dos faturamentos
menorF = min(faturamento)
maiorF = max(faturamento)
media = sum(faturamento) / len(faturamento)

#calculando os dias que o faturamento foi maior que a media mensal
acimaMedia = sum(1 for valor in faturamento if valor > media)

#imprimindo os resultados de faturamento
print("O menor valor do faturamento é de {}" .format(menorF))
print("O maior valor do faturamento é de {}" .format(maiorF))
print("O numero de dias com faturamento acima da media foram {} dias" .format(acimaMedia))




