# LINHA
def linha():
    print("=" * 50)

# LINHAS
def linhas(msg):
    linha()
    print(msg.center(50))
    linha()

# MENU
def listarOpcoes(lista):
    linhas("COPA DO MUNDO")
    for p, v in enumerate(lista):
        print(f"[{p+1}] - {v}")
    linha()
    opcao = int(input("Qual a sua opção: "))
    return opcao
    
# VERIFICA SE O NUMERO É INTEIRO
def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except:
            print("Erro! Digite um valor inteiro válido...")
        else:
            return n

#SAÍDA
from time import sleep
def saida():
    print("SAINDO...")
    sleep(1)
    print("OBRIGADO POR ME UTILIZAR :)")
    
nvEquipe=[]

# OPCAO 2 
def novaEquipe(eqp):
    situacao = True
    while situacao:
        dicionario = {}
        dicionario["pais"] = str(input("País: ")).upper()
        dicionario["abreviacao"] = str(input("Abreviação: ")).upper()
        dicionario["grupo"] = str(input("Grupo: ")).upper()
        nvEquipe.append(dicionario)
        print(dicionario)
        print(nvEquipe)
        while True:
            continuar = input("Desejar continuar? S/N: ").upper()[0]
            if continuar == "S":
                break
            elif continuar == "N":
                situacao = False
                break
            else:
                print("Opção inválida. Tente novamente...")
                continue

# OPCAO 3
def novoJogo(jgs):
    situacao = True
    while situacao:
        equipe1 = input("Equipe 1: ").upper()
        gols1 = leiaInt(f"Quantos gols {equipe1} fez?")
        faltas1 = leiaInt(f"Quantas faltas {equipe1} fez?")
        equipe2 = input("Equipe 2: ").upper()
        gols2 = leiaInt(f"Quantos gols {equipe2} fez?")
        faltas2 = leiaInt(f"Quantas faltas {equipe2} fez?")
        with open(jgs, "a") as jogo:
            jogo.write(f"{equipe1};{gols1};{faltas1};{equipe2};{gols2};{faltas2}\n")
        while True:
            continuar = input("Desejar continuar? S/N: ").upper()[0]
            if continuar == "S":
                break
            elif continuar == "N":
                print("Dados gravados com sucesso")
                situacao = False
                break
            else:
                print("Opção inválida. Tente novamente...")
                continue


# OPCAO 4
def numeroJogos(jgs):
    with open(jgs) as jogos:
        contador = 0
        for linha in jogos:
            contador += 1
        print(f"Número total de jogos: {contador}")

# OPCAO 5
def numeroEquipes(eqp):
    with open(eqp, "r") as equipes:
        contador = 0
        for linha in equipes:
            contador += 1
        print(f"Número total de equipes: {contador}")

# OPCAO 6
def gravarDados(jgs, eqp):
    '''with open(jgs, "a") as gravar:
        for x in "lista":
            gravar.write(f"{x}\n")'''
    with open(eqp, "a") as save:
        for y in nvEquipe:
            save.write(f"{y}\n")
    print("Dados gravados com sucesso.")

# OPCAO 7
def listarJogosEquipes(jgs, eqp):
    try:
        with open(jgs, "r") as jogos:
            for linha in jogos:
                times = linha.split(";")
                print(f"{times[0]} vs {times[3]}")
                print(f"GOLS {times[1]} x {times[4]}")
                print(f"FALTAS {times[2]} x {times[5]}")      
    except:
        print("O arquivo está vazio ou é inexistente.")
    else:
        print("=]")
    