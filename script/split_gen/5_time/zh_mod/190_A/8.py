def game(a,b,c):
    while True:
        if c == 0:
            if a == 0:
                return "Aoki"
            else:
                a -= 1
                c = 1
        else:
            if b == 0:
