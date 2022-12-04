# FELIPE BEZERRA BRAGA - BSI 22

from time import sleep
import funcoes

equipes = "equipes.txt"
jogos = "jogos.txt"

opc = ["Sair do programa", "Nova equipe", "Novo Jogo", "Número total de jogos salvos na copa", "Número total de equipes", "Gravar os dados", "Listar os jogos salvos e suas equipes"]

while True:
    opcao = funcoes.listarOpcoes(opc)
    if opcao == 1:
        funcoes.saida()
        break
    elif opcao == 2:
        funcoes.novaEquipe(equipes)
        sleep(2)
    elif opcao == 3:
        funcoes.novoJogo(jogos, equipes)
        sleep(2)
    elif opcao == 4:
        funcoes.numeroJogos(jogos)
        sleep(2)
    elif opcao == 5:
        funcoes.numeroEquipes(equipes)
        sleep(2)
    elif opcao == 6:
        funcoes.gravarDados(jogos, equipes)
        sleep(2)
    elif opcao == 7:
        funcoes.listarJogosEquipes(jogos, equipes)
        sleep(2)