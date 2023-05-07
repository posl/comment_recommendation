def main():
    N = int(input())
    Nstr = str(N)
    Nlen = len(Nstr)
    if Nlen < 4:
        print(0)
    else:
        Nlen -= 3
        print(Nlen + Nlen // 2)
