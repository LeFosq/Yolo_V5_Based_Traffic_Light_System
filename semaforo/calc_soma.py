def calculate_soma(file_path):
    with open("descrever.py") as f: #Executa o script que obtém e transcreve a imagem
     exec(f.read()) #Lê o .txt descrito na função
    file_path = "../semaforo/texto/arquivo.txt"
    file = open(file_path, "r")
    line = file.readline()
    line2 = file.readline() #Aqui dividimos o .txt por linhas, cada linha é referente a uma câmera (uma imagem analisada)
    words = line.split() #Dividimos a linha em palavras
    words2 = line2.split()
    n = len(words) #Obtemos o número de palavras em cada linha
    n2 = len(words2)
    soma = 0
    soma2 = 0
    for i in range(n): #Aqui é feita uma análise palavra a palavra, somente as que começam com cars,motorcycle,truck ou bus são contabilizadas na soma (entidades de interesse)
        if words[i].startswith("cars") or words[i].startswith("motorcycle") or words[i].startswith("truck") or words[i].startswith("bus"):
            soma = soma + int(words[i-1])
    for b in range(n2):
        if words2[b].startswith("cars") or words2[b].startswith("motorcycle") or words2[b].startswith("truck") or words2[b].startswith("bus"):
            soma2 = soma2 + int(words2[b-1])

    return soma, soma2 #Retornamos a soma de cada câmera para o código principal