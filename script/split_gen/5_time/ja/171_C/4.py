def base10to36(n):
    if (int(n/36)):
        return base10to36(int(n/36)) + str(n%36)
    else:
        return str(n%36)
n = int(input())
print(base10to36(n).replace("0", "a").replace("1", "b").replace("2", "c").replace("3", "d").replace("4", "e").replace("5", "f").replace("6", "g").replace("7", "h").replace("8", "i").replace("9", "j").replace("10", "k").replace("11", "l").replace("12", "m").replace("13", "n").replace("14", "o").replace("15", "p").replace("16", "q").replace("17", "r").replace("18", "s").replace("19", "t").replace("20", "u").replace("21", "v").replace("22", "w").replace("23", "x").replace("24", "y").replace("25", "z"))
