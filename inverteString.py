#função para inverter a palavra
def inverte_string(string):
    string_invert = ""
    for char in string:
        string_invert = char + string_invert
    return string_invert

#entrada da palavra do usuario
while True:
    palavraUsuario = input("Digite uma palavra para ela ser invertida ou digite 'sair' para finalizar o programa: ")
    if palavraUsuario.lower() == 'sair':
        break
    else:
        palavrainvert = inverte_string(palavraUsuario)
        #imprimindo a palavra invertida
        print("A palavra invertida é: {}" .format(palavrainvert))

