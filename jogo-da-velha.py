
def tabuleiro():
    linha = 0
    print("      0    1    2")
    for item in tabela:
        print(f"{linha} | {item}")
        linha += 1
    linha = 0

def jogadorX():
    print("Agora é a vez do jogador X")
    jogadaX = input().split()
    rowX = int(jogadaX[0])
    colunaX = int(jogadaX[1])
    while (rowX > 2 or rowX < 0) or (colunaX > 2 or colunaX < 0):
        print("jogada inválida")
        jogadaX = input().split()
        rowX = int(jogadaX[0])
        colunaX = int(jogadaX[1])


    tabela[rowX][colunaX] = "X"

def jogadorO():
    print("Agora é a vez do jogador O")
    jogadaO = input().split()
    rowO = int(jogadaO[0])
    colunaO = int(jogadaO[1])

    while (rowO > 2 or rowO < 0) or (colunaO > 2 or colunaO < 0):
        print("jogada inválida")
        jogadaO = input().split()
        rowO = int(jogadaO[0])
        colunaO = int(jogadaO[1])

    tabela[rowO][colunaO] = "O"

def diagonais():
    for item in tabela:
        if tabela[0][0] == tabela[1][1] == tabela[2][2] == "X":
            print("O jogador X ganhou!")
            return True
        if tabela[0][0] == tabela[1][1] == tabela[2][2] == "O":
            print("O jogador O ganhou!")
            return True
            # diagonal 1
        if tabela[0][2] == tabela[1][1] == tabela[2][0] == "X":
            print("O jogador X ganhou!")
            return True
        if tabela[0][2] == tabela[1][1] == tabela[2][0] == "O":
            print("O jogador O ganhou!")
            return True
            # diagonal 2

def linhas():
    for item in tabela:
        if tabela[0][0] == tabela[0][1] == tabela[0][2] == "X":
            print("O jogador X ganhou!")
            return True
        if tabela[0][0] == tabela[0][1] == tabela[0][2] == "O":
            print("O jogador O ganhou!")
            return True
            # reta 1
        if tabela[1][0] == tabela[1][1] == tabela[1][2] == "X":
            print("O jogador X ganhou!")
            return True
        if tabela[1][0] == tabela[1][1] == tabela[1][2] == "O":
            print("O jogador O ganhou!")
            return True
            # reta 2

def colunas():
    for item in tabela:
        if tabela[2][0] == tabela[2][1] == tabela[2][2] == "X":
            print("O jogador X ganhou!")
            return True
        if tabela[2][0] == tabela[2][1] == tabela[2][2] == "O":
            print("O jogador O ganhou!")
            return True
            # reta 3
        if tabela[0][0] == tabela[1][0] == tabela[2][0] == "X":
            print("O jogador X ganhou!")
            return True
        if tabela[0][0] == tabela[1][0] == tabela[2][0] == "O":
            print("O jogador O ganhou!")
            return True
            # coluna 1
        if tabela[0][1] == tabela[1][1] == tabela[2][1] == "X":
            print("O jogador X ganhou!")
            return True
        if tabela[0][1] == tabela[1][1] == tabela[2][1] == "O":
            print("O jogador O ganhou!")
            return True
            # coluna 2
        if tabela[0][2] == tabela[1][2] == tabela[2][2] == "X":
            print("O jogador X ganhou!")
            return True
        if tabela[0][2] == tabela[1][2] == tabela[2][2] == "O":
            print("O jogador O ganhou!")
            return True
            # coluna 3

def teste_velha():
    k = 0
    for item in tabela:
        for j in item:
            if j != " ":
                k += 1
    if k == 9:
        print("Velha!")
        return True

def teste_fim(fim):
    if teste_velha():
        fim = True
    if diagonais():
        fim = True
    if linhas():
        fim = True
    if colunas():
        fim = True

    return fim


tabela = [[" "," "," "],[" "," "," "],[" "," "," "]]
i = 0
print("JOGO DA VELHA")
print("-------INSTRUÇÕES------")
print("Para jogar digite dois números separados por um espaço. O primeiro número deve indicar a linha e o segundo deve indicar a coluna")
print("o jogador X começa jogando!")
linha = 0
fim = False
tabuleiro()

while not fim:

    jogadorX()

    tabuleiro()

    fim = teste_fim(fim)
    if fim:
        break

    jogadorO()

    tabuleiro()

    fim = teste_fim(fim)
    if fim:
        break




