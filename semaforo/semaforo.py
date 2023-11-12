from calc_soma import calculate_soma
import time

def temporizador(segundos): #Função utilizada para temporizar os semáforos
    try:
        for i in range(segundos, 0, -1):
            print(f"Tempo restante: {i} segundos")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Fim forçado")

def print_color(text, color_code): #Altera a cor do texto no console
    print(f"\033[{color_code}m{text}\033[0m")
def semaforo(valor): #Lógica semafórica simples, baseada em um switch com 4 possibilidades para dois semáforos que estão posicionados em um cruzamento
    switch = {
        1: ververm,
        2: amverm,
        3: vermver,
        4: vermam
    }
    switch.get(valor, default)()
def ververm():
    soma,soma2 = calculate_soma("../testes/texto/arquivo.txt") #Aqui acionamos a função que calcula as somas, que aciona todos os outros componentes
    semaforo1 = "verde"
    semaforo2 = "vermelho"
    print_color("semaforo1", "32")
    print_color("semaforo2", "31")
    print("-----------------------")
    if soma > soma2:
        temporizador(15)
        semaforo(2)
    else:
        temporizador(10)
        semaforo(2)

def amverm():
    semaforo1 = "amarelo"
    semaforo2 = "vermelho"
    print_color("semaforo1", "33")
    print_color("semaforo2", "31")
    print("-----------------------")
    temporizador(5)
    semaforo(3)

def vermver():
    soma, soma2 = calculate_soma("../testes/texto/arquivo.txt")
    semaforo1 = "vermelho"
    semaforo2 = "verde"
    print_color("semaforo1", "31")
    print_color("semaforo2", "32")
    print("-----------------------")
    if soma > soma2:
        temporizador(10)
        semaforo(4)
    else:
        temporizador(15)
        semaforo(4)

def vermam():
    semaforo1 = "vermelho"
    semaforo2 = "amarelo"
    print_color("semaforo1", "31")
    print_color("semaforo2", "33")
    print("-----------------------")
    print("Fim do ciclo")
    temporizador(5)
    semaforo(1)

def default(): #"Estado" que nunca será utilizado e por isso é tratado como erro
    print_color("ERRO ERRO ERRO", "31")

ligar = input("Deseja ligar o semáforo? [sim] para iniciar: ")
if ligar == "sim":
    semaforo(1)