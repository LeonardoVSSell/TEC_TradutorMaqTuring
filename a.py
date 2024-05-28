# Lista de strings
lista = ['01010', '10100', '00101', '11111']

# Percorrendo a lista
for i in range(len(lista)):
    # Verificando se o primeiro caractere é '0' e substituindo por "0'"
    if lista[i][0] == '0':
        lista[i] = "0'" + lista[i][1:]
    
    # Verificando se o último caractere é '0' e substituindo por "'0"
    if lista[i][-1] == '0':
        lista[i] = lista[i][:-1] + "0'"

# Exibindo a lista modificada
print(lista)
