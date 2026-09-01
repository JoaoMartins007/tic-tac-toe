import random

def desenhar_tabuleiro(tab):
        print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
        print("---|---|---")
        print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
        print("---|---|---")
        print(f" {tab[6]} | {tab[7]} | {tab[8]} ")

def verificar(tab,simbolo):
        vitorias = [[0,1,2],[3,4,5],[6,7,8],
                    [0,3,6],[1,4,7],[2,5,8],
                    [0,4,8],[2,4,6]]
        for condições in vitorias:
            if tab[condições[0]] == simbolo and tab[condições[1]] == simbolo and tab[condições[2]] == simbolo:
                return True
        return False

while True:
    tab =[' ',' ',' ',' ',' ',' ',' ',' ',' ']

    print("\nEscolha o modo de jogo:")
    print("\n1: 1 jogador      2: 2 jogadores")
    opção= int(input("\n"))
    if opção == 2:
        X = 0
        O = 0
        while True:
            jogador_atual = 'X'
            
            for turno in range(9):
                print(f"\nÉ a vez do jogador {jogador_atual}")
                desenhar_tabuleiro(tab)
                while True:
                    resposta = int(input(f"Escolha uma posição de 1 a 9:")) -1
                    if resposta <0 or resposta >8:
                        print("Essa posição não existe")
                    elif tab[resposta]==' ':
                        break
                    else:
                        print("Essa posição está ocupada")
                        desenhar_tabuleiro(tab)
                tab[resposta] = jogador_atual
                
                

                if verificar(tab,jogador_atual)==True:
                    print(f"O jogo acabou, o vencedor é {jogador_atual}")
                    desenhar_tabuleiro(tab)
                    if jogador_atual == 'X':
                        X+=1
                    else:
                        O+=1
                    break
                if jogador_atual == 'X':
                        jogador_atual = 'O'
                else:
                        jogador_atual ='X'

            else:
                print("O jogo acabou num empate")
                desenhar_tabuleiro(tab)
            print(f"Resultado:")
            print(f"\nX={X} e O={O}")
            print("\nDeseja jogar outra vez ou mudar de modo?")
            print("1:Mudar  2:Jogar outra vez")
            opção_2 = int(input())
            if opção_2 ==2:
                tab =[' ',' ',' ',' ',' ',' ',' ',' ',' ']
            else:
                break




    if opção ==1:
        Jogador = 0
        Máquina = 0
        while True:
            disponiveis =[0,1,2,3,4,5,6,7,8]

            for turnos in range(5):
                print("\n")
                desenhar_tabuleiro(tab)
                print("\n")
                while True:
                    resposta = int(input("Escolhe uma posição de 1 a 9 :  ")) - 1
                    if resposta <0 or resposta >8:
                        print("Essa posição não existe")
                    elif tab[resposta]== ' ':
                        break
                    else:
                        print("Essa posição está ocupada")
                tab[resposta] = 'X'
                disponiveis.remove(resposta)
                if disponiveis !=[]:
                    robo = random.choice(disponiveis)
                    disponiveis.remove(robo)
                    tab[robo]= 'O'

                if verificar(tab,'X') == True:
                    print("Ganhaste!!")
                    desenhar_tabuleiro(tab)
                    Jogador+=1
                    break
                if verificar(tab,'O') == True:
                    print("Perdeste.")
                    desenhar_tabuleiro(tab)
                    Máquina+=1
                    break
            else:
                print("O jogo empatou")
                desenhar_tabuleiro(tab)
            print(f"Resultado:")
            print(f"\nJogador={Jogador} e Máquina={Máquina}")
            print("\nDeseja jogar outra vez ou mudar de modo?")
            print("1:Mudar  2:Jogar outra vez")
            opção_1 = int(input())
            if opção_1 ==2:
                tab =[' ',' ',' ',' ',' ',' ',' ',' ',' ']
            else:
                break
        
            
    
