def main():
    S = input()
    L = len(S)
    if L > 10:
        print("No")
        return
    if L == 1:
        if S == "o":
            print("Yes")
        else:
            print("No")
        return
    if L == 2:
        if S == "ox" or S == "xo":
            print("Yes")
        else:
            print("No")
        return
    if L == 3:
        if S == "oxx" or S == "xox" or S == "xxo":
            print("Yes")
        else:
            print("No")
        return
    T = "oxx" + "xox" + "xxo"
    if L == 4:
        if S == T:
            print("Yes")
        else:
            print("No")
        return
    if L == 5:
        if S == T + "oxx" or S == T + "xox" or S == T + "xxo":
            print("Yes")
        else:
            print("No")
        return
    if L == 6:
        if S == T + "oxx" + "xox" or S == T + "xox" + "xxo" or S == T + "xxo" + "oxx":
            print("Yes")
        else:
            print("No")
        return
    if L == 7:
        if S == T + "oxx" + "xox" + "xxo" or S == T + "xox" + "xxo" + "oxx" or S == T + "xxo" + "oxx" + "xox":
            print("Yes")
        else:
            print("No")
        return
    if L == 8:
        if S == T + "oxx" + "xox" + "xxo" + "oxx" or S == T + "xox" + "xxo" + "oxx" + "xox" or S == T + "xxo" + "oxx" + "xox" + "xxo":
            print("Yes")
        else:
            print("No")
        return
    if L == 9:
        if S == T + "oxx" + "xox
