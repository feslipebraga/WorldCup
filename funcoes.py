# LINHA
def linha():
    print("=" * 50)

# LINHA2
def linha2():
    print("-" * 50)

# LINHAS
def linhas(msg):
    linha()
    print(msg.center(50))
    linha()

# MENU
valores = list(range(1, 7+1))
def listarOpcoes(lista):
    linhas("COPA DO MUNDO DA FIFA™")
    for p, v in enumerate(lista):
        print(f"[{p+1}] - {v}")
    linha()
    while True:
        opcao = leiaInt("Qual a sua opção: ")
        if opcao not in valores:
            print("Opção inválida, digite uma entre 1 e 7")
            continue
        else:
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

# OPCAO 2 
equipe = []
aux2 = []
pais2 = []
def novaEquipe(eqp):
    situacao = True
    while situacao:
        while True:
            pais = str(input("País: ")).capitalize()
            if pais in pais2:
                print("País já está salvo no banco de dados. Tente outro!")
                continue
            else:
                break
        abreviacao = str(input("Abreviação: ")).upper()
        grupo = str(input("Grupo: ")).upper()
        pais2.append(pais)
        aux2.append(pais)
        aux2.append(abreviacao)
        aux2.append(grupo)
        equipe.append(aux2[:])
        aux2.clear()
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
times = []
jogos = []
aux3 = []
def novoJogo(jgs, eqp):
    try:
        with open(eqp, "r") as equipes:
                for x in equipes.readlines():
                    y = x.split(';')
                    times.append(y[0])
        situacao = True
        while situacao:
            # equipe 1
            equipe1 = input("Equipe 1: ").capitalize()
            verdade = equipe1 in times
            falso = equipe1 not in times
            if verdade:
                gols1 = leiaInt(f"Quantos gols {equipe1} fez? ")
                faltas1 = leiaInt(f"Quantas faltas {equipe1} fez? ")
            elif falso:
                print("O time não se encontra em nosso banco de dados. Adicione-o ou tente colocar outro.")
                continue
            # equipe 2
            while True:
                equipe2 = input("Equipe 2: ").capitalize()
                verdade2 = equipe2 in times
                falso2 = equipe2 not in times
                if equipe2 == equipe1:
                    print("Time em duplicidade, tente outro.")
                    continue
                elif verdade2:
                    gols2 = leiaInt(f"Quantos gols {equipe2} fez? ")
                    faltas2 = leiaInt(f"Quantas faltas {equipe2} fez? ")
                    break
                elif falso2:
                    print("O time não se encontra em nosso banco de dados. Adicione-o ou tente colocar outro.")
                    continue
            aux3.append(equipe1)
            aux3.append(gols1)
            aux3.append(faltas1)
            aux3.append(equipe2)
            aux3.append(gols2)
            aux3.append(faltas2)
            jogos.append(aux3[:])
            aux3.clear()
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
    except FileNotFoundError:
        print("Para criar jogos é necessário criar uma equipe primeiramente. Digite a opção 2!")                

# OPCAO 4
def numeroJogos(jgs):
    try:
        with open(jgs) as jogos:
            contador = 0
            for linha in jogos.readlines():
                contador += 1
            print(f"Número total de jogos salvos: {contador}")
    except FileNotFoundError:
        print("Não existem jogos. Digite a opção 3 para criá-los!") 

# OPCAO 5
def numeroEquipes(eqp):
    try:
        with open(eqp, "r") as equipes:
            contador = 0
            for linha in equipes.readlines():
                contador += 1
            print(f"Número total de equipes salvas: {contador}")
    except FileNotFoundError:
        print("Não existem equipes. Digite a opção 2 para criá-las!") 

# OPCAO 6
def gravarDados(jgs, eqp):
    with open(jgs, "a") as gravar:
        for linha in jogos:
            for elemento in linha:
                gravar.write(f"{elemento};")
            gravar.write("\n")
    with open(eqp, "a") as save:
        for l in equipe:
            for e in l:
                save.write(f"{e};")
            save.write("\n")
    print("Dados gravados com sucesso.")

# OPCAO 7
grupos = []
aux7 = []
teste = []
def listarJogosEquipes(jgs, eqp):
    try:
        # Mostra os times salvos
        with open(jgs, "r") as games, open(eqp, "r") as teams:
            print("TIMES SALVOS".center(50))
            sleep(2)
            for x in teams.readlines():
                equipes7 = x.split(";")
                print(f"{equipes7[0]:.<15} {equipes7[1]:<15} {'GRUPO':>15}:{equipes7[2]:>2}")
                sleep(0.5)
            linha2()
        # Mostra os jogos salvos.
            print("JOGOS SALVOS".center(50))
            cont = 0
            for c in games.readlines():
                jogos7 = c.split(";")
                cont += 1
                print(f'\033[31m{"JOGO":<10} {"GOLS":>10} {"FALTAS":>20}\033[m')
                print(f"{jogos7[0]:<10} {jogos7[1]:>9} {jogos7[2]:>18}")
                print(f"{jogos7[3]:<10} {jogos7[4]:>9} {jogos7[5]:>18}")
                print()
                sleep(2)
            print(f"Ao total, foram listados {cont} jogos.")
            sleep(2)
    except FileNotFoundError:
        print("O arquivo não existe. Digite a opção 2 para criar equipes e 3 para joogs!") 