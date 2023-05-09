def main():
    S = input()
    #c, h, o, k, u, d, a, i
    c = 0
    ch = 0
    cho = 0
    chok = 0
    choku = 0
    chokud = 0
    chokuda = 0
    chokudai = 0
    for s in S:
        if s == "c":
            c += 1
        elif s == "h":
            ch += c
        elif s == "o":
            cho += ch
        elif s == "k":
            chok += cho
        elif s == "u":
            choku += chok
        elif s == "d":
            chokud += choku
        elif s == "a":
            chokuda += chokud
        elif s == "i":
            chokudai += chokuda
    print(chokudai % (10**9 + 7))
