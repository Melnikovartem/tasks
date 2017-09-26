__author__ = "hi_melnikov"

def x_and_o(game_inp):
    diagonals = [''.join([game_inp[n][n] for n in range(3)]), ''.join([game_inp[n][2-n] for n in range(3)])]
    vertical = [''.join([game_inp[j] [i] for j in range(3)]) for i in range(3)]
    all_check = game_inp + vertical + diagonals
    variants = map(lambda line : line[0] if len(set(line)) == 1 else -1 , all_check)
    ans = list(filter(lambda x: x != -1, variants))
    if len(ans) == 1:
        return ans[0] if ans[0] != "." else "D"
    else:
        return "D"
    
    

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
