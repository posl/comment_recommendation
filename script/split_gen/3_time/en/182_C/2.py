def main():
    N = input()
    l = len(N)
    if l == 1:
        if int(N) % 3 == 0:
            print(0)
        else:
            print(-1)
        return
    if l == 2:
        if int(N) % 3 == 0:
            print(0)
        else:
            if int(N[0]) % 3 == 0 or int(N[1]) % 3 == 0:
                print(1)
            else:
                print(-1)
        return
    n = [int(s) for s in N]
    s = sum(n)
    if s % 3 == 0:
        print(0)
        return
    if s % 3 == 1:
        if l == 3:
            if 1 in n:
                print(1)
            else:
                print(-1)
            return
        else:
            if 1 in n:
                print(1)
                return
            else:
                if 2 in n and l > 4:
                    print(2)
                    return
                else:
                    print(-1)
                    return
    else:
        if l == 3:
            if 2 in n:
                print(1)
            else:
                print(-1)
            return
        else:
            if 2 in n:
                print(1)
                return
            else:
                if 1 in n and l > 4:
                    print(2)
                    return
                else:
                    print(-1)
                    return
main()
