__author__ = "hi_melnikov"

def x_and_o(game_inp):
    winner = "D"
    winners = []
    size = 3
    
    game = []
    for line in game_inp:
        game.append(list(line))
    

    # проходимся по всем вертикалям
    for i in range(size):
        status = True
        last = game[i][0]
        for j in range(1, size):
            if last != game[i][j]:
                status = False
            else:
                last = game[i][j]
        if status:
            winners.append(last)
    # вертикалям(Ctrl+C; Ctrl+V)
    for j in range(size):
        status = True
        last = game[0][j]
        for i in range(1, size):
            if last != game[i][j]:
                status = False
            else:
                last = game[i][j]
        if status:
            winners.append(last)
                
    # по диагоналям
    for diag in [True, False]:
        status = True
        if diag:
            last = game[0][0]
        else:
            last = game[0][size-1]
        for i in range(1, size):
            if diag:
                j = i
            else:
                j = size - i - 1
            if last != game[i][j]:
                status = False
            else:
                last = game[i][j]
        if status:
            winners.append(last)

        if len(winners) == 1 and winners[0] != '.':
            winner = winners[0]
            
    return winner

if __name__ == "__main__":
    test1 = x_and_o([
    "X.O",
    "XX.",
    "XOO"]) == "X"
    
    test2 = x_and_o([
    "OO.",
    "XOX",
    "XOX"]) == "O"
    
    test3 = x_and_o([
    "OO.",
    "XOX",
    "XOX"]) == "O"

    test4 = x_and_o([
        "XO.",
        "OX.",
        "OOX",
        ]) == "X"
    
    test5 = x_and_o([
        "OOX",
        "OX.",
        "XO.",
        ]) == "X"
    
    test6 = x_and_o([
        "OOX",
        "OXX",
        "OXX",
        ]) == "D"
    
    test7 = x_and_o([
        "X.O",
        "O.X",
        "O.X",
        ]) == "D"
    if test1 and test2 and test3 and test4 and test5 and test6 and test7:
        print("Fine")
    else:
        print("Error") 
