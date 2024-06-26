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
nome_arquivo = '/home/leonardo/Documentos/2024_01/TEC/TEC_TrautorMaqTuring/testes/sameamount10.txt'

linhas = ler_arquivo_para_lista(nome_arquivo)

if(linhas[0]==';S'):
    #primeiro marcar todos os estados de entrada e saida que são 0 como §
    for i in range(len(linhas)):
        if linhas[i][0] == '0':
            linhas[i] = "§" + linhas[i][1:]
        if linhas[i][-1] == '0':
            linhas[i] = linhas[i][:-1] + "§"

    #criar um novo estado 0 com as regras do que fazemos primeiro e depois ir para ao estado §
    linhas.append('0 0 0 l 0')
    linhas.append('0 1 1 l 0')
    linhas.append("0 _ # r §")

    #adicionar em cada estado novo, a regra que se le # so imprime # e vai para direita e vai 
    #para o estado que foi enviado antes
    destinos = []
    for i in range(len(linhas)-1):
        i+1
        if 'l' in linhas[i]:#achamos a transição para l
            caracteres = linhas[i].split()
            if(caracteres[3]=='l'):
                destinos.append(caracteres[4])
    destinos = list(set(destinos))
    for i in destinos:
        linhas.append(i + " # # r "+ i)

    #montar o novo arquivo
    removido = linhas.pop(0)
    with open('outDuplamenteInfinita.txt', 'w') as arquivo:
    # Escreva cada elemento da lista no arquivo, separado por espaços
        for elemento in linhas:
            arquivo.write(elemento + '\n')

if(linhas[0]==';I'):
    #Primeiro marcar todos os estados de entrada e saida que são 0 como §
    for i in range(len(linhas)):
        if linhas[i][0] == '0':
            linhas[i] = "§" + linhas[i][1:]
        if (linhas[i][-1] == '0' and linhas[i][-2]!='1'):
            linhas[i] = linhas[i][:-1] + "§"

    #para a direita
    destinos = []
    for i in range(len(linhas)-1):
        j=i+1
        if 'r' in linhas[j]:#achamos a transição para l
            caracteres = linhas[j].split()
            if(caracteres[3]=='r'):
                destinos.append(caracteres[4])
    destinos = list(set(destinos))
    for i in destinos:
        destinoModificado = i + "%"
        linhas.append(i + " & _ r "+ destinoModificado)
        linhas.append(destinoModificado + " _ & l "+ i)

    #agora, toda vez que temos uma transição para esquerda, verificamos se o simbolo lido é #
    #se for desloca toda a palavra para a direita, coloca um branco entre a palavra e o #, 
    #com cabeçote nesse branco e mantendo ao estado destino que nos fez ir para a esquerda
    destinos = []
    for i in range(len(linhas)-1):
        j=i+1
        if 'l' in linhas[j]:#achamos a transição para l
            caracteres = linhas[j].split()
            destinos.append(caracteres[4])
    destinos = list(set(destinos))
    for i in destinos:
        destinoModificado = i + "@"
        linhas.append(i + " # # r "+ destinoModificado)
        #este destino modificado joga tudo para direita
        #ida
        linhas.append(destinoModificado+' 1 O r '+destinoModificado)
        linhas.append(destinoModificado+' 0 Z r '+destinoModificado)
        linhas.append(destinoModificado+' _ W r '+destinoModificado)
        #final
        destinoModificadoA = destinoModificado + "A"
        linhas.append(destinoModificado+' & $ r '+destinoModificadoA)
        linhas.append(destinoModificadoA+' _ & l '+destinoModificado)
        linhas.append(destinoModificado+' $ _ l '+destinoModificado)
        #volta
        destinoModificadoZ = destinoModificado + "Z"
        linhas.append(destinoModificado+' Z $ r '+destinoModificadoZ)
        linhas.append(destinoModificadoZ+' _ 0 l '+destinoModificado)
        destinoModificadoU = destinoModificado + "U"
        linhas.append(destinoModificado+' O $ r '+destinoModificadoU)
        linhas.append(destinoModificadoU+' _ 1 l '+destinoModificado)
        destinoModificadoB = destinoModificado + "Br"
        linhas.append(destinoModificado+' W $ r '+destinoModificadoB)
        linhas.append(destinoModificadoB+' _ _ l '+destinoModificado)
        #comeco
        destinoModificadoFinal = destinoModificado + "F"
        linhas.append(destinoModificado+' # # r '+destinoModificadoFinal)
        linhas.append(destinoModificadoFinal+' _ _ l '+destinoModificadoFinal)
        linhas.append(destinoModificadoFinal+' # # r '+i)
    linhas = list(set(linhas))

    #Ajustar estado inicial
    #Temos que empurrar tudo para a direita, marcar os limites da palavra e voltar ao estado 
    #inicial para processar
    #Consideramos o final da palavra quando lemos dois brancos seguidos.
    linhas.append('0 1 O r 0')
    linhas.append('0 0 Z r 0')
    linhas.append('0 _ $ r A')
    linhas.append('A _ & l 0')
    linhas.append('0 $ _ l 0')
    linhas.append('0 Z $ r Zero')
    linhas.append('Zero _ 0 l 0')
    linhas.append('0 O $ r Um')
    linhas.append('Um _ 1 l 0')
    linhas.append("A 1 1 l A")
    linhas.append("A 0 0 l A")
    linhas.append("A $ # r §")

    #montar o novo arquivo
    with open('outSispser.txt', 'w') as arquivo:
    # Escreva cada elemento da lista no arquivo, separado por espaços
        for elemento in linhas:
            arquivo.write(elemento + '\n')