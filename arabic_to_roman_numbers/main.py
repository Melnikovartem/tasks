def roman(numer):
    result = ""
    values = [
        (10, "X"),
        (5, "V"),
        (1, "I")
        ]
    val_numer = []
    numer_count = numer
    for val in values:
        add = numer_count//val[0]
        if add < 4:
            result += val[1]*add
            numer_count -= add*val[0] 
        else:
            result += val[1]*(add-3) + roman(numer + val[0])
            numer_count -= (add-3)*val[0] 
    return result
            



if __name__=="__main__":
    tests = [
            (1, "I"),
            (2, "II"),
            (3, "III"),
            (4, "IV"),
            (5, "V"),
            (6, "VI"),
            (7, "VII"),
            (8, "VIII"),
            (9, "IX"),
            (10, "X"),
            ]
    
    for test in tests:
        if roman(test[0]) != test[1]:
            print("Error on", test [0], roman(test[0])
                    , "instead of", test[1])
    print("END")
