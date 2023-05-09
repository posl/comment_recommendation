def main():
    N = int(input())
    Nstr = str(N)
    Nlen = len(Nstr)
    Nsum = sum(map(int, Nstr))
    if Nsum % 3 == 0:
        print(0)
        return
    if Nsum % 3 == 1:
        if "1" in Nstr or "4" in Nstr or "7" in Nstr:
            if Nlen == 1:
                print(-1)
                return
            print(1)
            return
        if Nlen == 2:
            print(-1)
            return
        print(2)
        return
    if Nsum % 3 == 2:
        if "2" in Nstr or "5" in Nstr or "8" in Nstr:
            if Nlen == 1:
                print(-1)
                return
            print(1)
            return
        if Nlen == 2:
            print(-1)
            return
        print(2)
        return
