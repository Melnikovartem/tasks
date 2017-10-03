def roman():
    return "I"

if __name__=="__main__":
    tests = [
            (1, "I"),
            (2, "II"),
            (3, "III"),
            (4, "VI"),
            (5, "V")
            ]
    for test in tests:
        if roman(test[1]) != test[2]:
            print("Error on", test [1], roman(test[1])
                    , "instead of", test[2])
    print("END")
