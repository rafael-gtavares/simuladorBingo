#Grupo: Caio Honório, Davi Honório, Guilherme Duarte, Rafael Tavares e Victor Lessa

from random import randint

# a) Gerar automaticamente 100 cartelas do bingo

cartelas_bingo = [] #Lista de matrizes - irá armazenar as 100 cartelas
numCartelas = 100
numLinhas = 5
numColunas = 5
i = 0
while i < numCartelas:
    # Gera uma cartela com todos os números diferentes
    cartela_candidata = [] #Cria uma lista vazia para armazenar uma nova cartela que está sendo gerada.
    numeros_cartela = [] #Essa lista vai guardar todos os números que já foram adicionados à cartela_candidata, para não ter números repetidos na cartela
    for j in range(numLinhas): #Formar a matriz da cartela
        linha_cartela = []
        for k in range(numColunas):
            numero_aleatorio = randint(0, 99) #Gera um número aleatório de 0 a 99
            
            numero_repetido = True #Essa variavél vai indicar se o número gerado já existe em numeros_cartela. Começa em True pois ele sempre precisa verificar pelo menos uma vez
            while numero_repetido: #Enquanto numero_repetido for verdadeiro, ele gera um novo número
                numero_aleatorio = randint(0, 99)
                numero_repetido = False
                for n in numeros_cartela: #Percorre todos os itens da lista numeros_cartela para verificar se o número recém-gerado já foi gerado anteriormente
                    if n == numero_aleatorio:
                        numero_repetido = True #Com numero_repetido sendo True, ele vai gerar novamente, voltando no início do while

            linha_cartela.append(numero_aleatorio) #Adiciona o número à linha_cartela
            numeros_cartela.append(numero_aleatorio) #Adiciona o mesmo número à lista dos números que já foram gerados
        cartela_candidata.append(linha_cartela) # Adiciona a linha na cartela

    # Confirmando que não terá cartelas iguais:
    cartela_repetida = False
    for cartela in cartelas_bingo: #Percorre todas as cartelas na lista de cartelas
        if cartela == cartela_candidata: #Verifica se a cartela candidata é igual a alguma tabela existente em cartelas_bingos
            cartela_repetida = True

    if cartela_repetida == False: #Caso a cartela_candidata seja falsa, significa que ele não é repetido
        cartelas_bingo.append(cartela_candidata)
        i+=1

print("Todas as 100 cartelas foram geradas!")



# b) Sorteio dos números e verificação dos vencedores

numeros_sorteados = [] #Armazena os números sorteados
vencedores_linha = [] #Armazena o índice da(s) primeira(s) cartela(s) que completar uma linha
vencedores_coluna = [] #Armazena o índice da(s) primeira(s) cartela(s) que completar uma coluna
vencedores_cartela_completa = [] #Armazena o índice da(s) primeira(s) cartela(s) que completaram todos os 25 números
fim_de_jogo = False #Variável que vai decretar o fim do jogo, quando mudar para True, o sorteio irá parar

numeros_possiveis = [] #Cria uma lista com todos os números de 0 a 99 para o sorteio
for i in range(100):
    numeros_possiveis.append(i)

# Loop principal, onde os números são sorteados e as cartelas são verificadas a cada rodada.
while fim_de_jogo == False and len(numeros_possiveis) > 0: #Enquanto o jogo não tiver terminado e ainda houver números para sortear
    
    # Sorteia um número que ainda não saiu
    indice_sorteado = randint(0, len(numeros_possiveis) - 1) #Sorteia o INDÍCE de um número na lista numeros_possiveis // -1 devido ao 0
    numero_da_vez = numeros_possiveis[indice_sorteado] #Pega o número que está no índice sorteado acima
    numeros_sorteados.append(numero_da_vez) #Adiciona o número na lista dos números sorteados
    del(numeros_possiveis[indice_sorteado]) #Remove o número sorteado da lista de possibilidades (para não repetir)

    print(f"\nNúmero sorteado: {numero_da_vez}")

    # Parte da verificação dos vencedores
    indice_cartela = 0 #Indica qual cartela estamos verificando
    for cartela_atual in cartelas_bingo:

        #- Verificação de Linha:
        if len(vencedores_linha) == 0: #Verifica se ainda não há um vencedor para a linha
            for i in range(numLinhas): #Percorre as 5 linhas da cartela_atual
                contador_linha = 0 #Zera o contador para cada nova linha ser verificada
                for j in range(numColunas): #Percorre os números da linha
                    numero_da_cartela = cartela_atual[i][j] #Acessa o número na posição [linha][coluna] da matriz e o armazena na variável
                    #if numero_da_cartela in numeros_sorteados: # Verifica se o número da cartela está na lista de sorteados
                    encontrado = False
                    for numero_sorteado in numeros_sorteados:
                        if numero_da_cartela == numero_sorteado and encontrado == False:
                            encontrado = True
                            contador_linha+=1
                
                if contador_linha == numColunas:
                    vencedores_linha.append(indice_cartela) #Adiciona o índice da cartela vencedora em vencedores_linha

        #- Verificação de Coluna:
        if len(vencedores_coluna) == 0:
            for j in range(numColunas):
                contador_coluna = 0
                for i in range(numLinhas):
                    numero_da_cartela = cartela_atual[i][j]
                    #if numero_da_cartela in numeros_sorteados:
                    encontrado = False
                    for numero_sorteado in numeros_sorteados:
                        if numero_da_cartela == numero_sorteado and encontrado == False:
                            encontrado = True
                            contador_coluna+=1

                if contador_coluna == numLinhas:    
                    vencedores_coluna.append(indice_cartela)
        
        #- Verificação de Cartela Completa:
        contador_cartela_completa = 0 #Contador que serve para contar quantos números da cartela atual foram sorteados. Esse contador é zerado para cada nova cartela analisada
        for linha_cartela in cartela_atual: #Percorre cada linha da cartela_atual
            for numero_da_cartela in linha_cartela: #Percorre cada número da linha da cartela_atual
                #if numero_da_cartela in numeros_sorteados: #Verifica se o número está nos números sortedos
                encontrado = False
                for numero_sorteado in numeros_sorteados:
                    if numero_da_cartela == numero_sorteado and encontrado == False:
                        encontrado = True
                        contador_cartela_completa+=1
        
        num_total_cartela = numColunas * numLinhas #Número total de itens da cartela
        if contador_cartela_completa == num_total_cartela: #Se todos os números da cartela foram sorteados, esta é uma cartela vencedora do bingo
            cartela_ja_ganhou = False # Verifica se essa cartela já não foi adicionada
            for vencedor in vencedores_cartela_completa:
                if vencedor == indice_cartela:
                    cartela_ja_ganhou = True

            if cartela_ja_ganhou == False:
                vencedores_cartela_completa.append(indice_cartela) #Adiciona o índice da cartela vencedora
            fim_de_jogo = True # O jogo termina quando a primeira cartela é completada

        indice_cartela+=1
    
#- Imprimindo os resultados:

print("\n\n--- FIM DE JOGO ---")

# Mostra a(s) cartela(s) que acertaram a linha

print("\n--- VENCEDOR(ES) DA LINHA ---")
for i in vencedores_linha:
    print(f"Cartela Vencedora (Linha) - Numero {i + 1}:")
    for linha_vencedora in cartelas_bingo[i]:
        print(linha_vencedora)


# Mostra a(s) cartela(s) que acertaram a coluna

print("\n--- VENCEDOR(ES) DA COLUNA ---")
for i in vencedores_coluna:
    print(f"Cartela Vencedora (Coluna) - Numero {i + 1}:")
    for linha_vencedora in cartelas_bingo[i]:
        print(linha_vencedora)


# Mostra a(s) cartela(s) vencedora(s) do jogo
print("\n--- VENCEDOR(ES) DO BINGO (CARTELA COMPLETA) ---")
for i in vencedores_cartela_completa:
    print(f"Cartela Vencedora (Bingo) - Numero {i + 1}:")
    for linha_vencedora in cartelas_bingo[i]:
        print(linha_vencedora)