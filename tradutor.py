# Função para ler um arquivo de texto e retornar uma lista de palavras de cada linha
def ler_arquivo_para_lista(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            # Remove o caractere de nova linha de cada linha
            linhas = [linha.strip() for linha in linhas]
            return linhas
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")
        return []

# Nome do arquivo que será lido
nome_arquivo = '/home/leonardo/Documentos/2024_01/TEC/TEC_TrautorMaqTuring/testes/odd.txt'

# Chama a função para ler o arquivo e obter a lista de palavras por linha
linhas = ler_arquivo_para_lista(nome_arquivo)

if(linhas[0]==';S'):
    #primeiro marcar todos os estados de entrada e saida que são 0 como 0'(feito)
    for i in range(len(linhas)):
        if linhas[i][0] == '0':
            linhas[i] = "0'" + linhas[i][1:]
        if linhas[i][-1] == '0':
            linhas[i] = linhas[i][:-1] + "0'"
    #for i, transicao in enumerate(linhas):
    #    print(transicao)

    #criar um novo estado 0 com as regras do que fazemos primeiro e depois ir para ao estado 0'(feito)
    #print(linhas)
    linhas.append('0 0 0 l 0')
    linhas.append('0 1 1 l 0')
    linhas.append("0 _ # r 0'")
    #print(linhas)

    #adicionar em cada estado novo a regra que se le # so imprime # e vai para direita e vai 
    #para o estado que foi enviado antes
    destinos = []
    for i in range(len(linhas)-1):
        i+1
        if 'l' in linhas[i]:#achamos a transição para l
            caracteres = linhas[i].split()
            if(caracteres[3]=='l'):
                destinos.append(caracteres[4])
    destinos = list(set(destinos))
    #print(destinos)
    for i in destinos:
        linhas.append(i + " # # r "+ i)
    #print(linhas)

    #montar o novo arquivo(feito)
    with open('out.txt', 'w') as arquivo:
    # Escreva cada elemento da lista no arquivo, separado por espaços
        for elemento in linhas:
            arquivo.write(elemento + '\n')
