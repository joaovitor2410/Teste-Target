#faturamento dos estados
faturamento = {
'SP' : 67836.43,
'RJ' : 36678.66,
'MG' : 29229.88,
'ES' : 27165.48,
'Outros' : 19849.53
}

#calculando o total dos faturamentos da empresa
Ftotal = sum(faturamento.values())

#calculando as porcentagens de cada estado
percentuais= {}
for estado, valor in faturamento.items():
    porcentagem = (valor / Ftotal) * 100
    percentuais[estado] = f"{porcentagem:.2f}%"

#imprimindo o percentual de faturamento de cada estado
for estado, porcentagem in percentuais.items():
    print("O estado de {} representa {} do faturamento total." .format(estado,porcentagem))


