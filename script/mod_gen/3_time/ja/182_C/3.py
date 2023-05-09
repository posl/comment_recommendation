def main():
    N = input()
    N = list(N)
    N = list(map(int,N))
    k = len(N)
    if k == 1:
        if N[0] % 3 == 0:
            print(0)
        else:
            print(-1)
        return
    elif k == 2:
        if (N[0] + N[1]) % 3 == 0:
            print(0)
        elif (N[0] * 10 + N[1]) % 3 == 0:
            print(0)
        elif (N[0] + N[1] * 10) % 3 == 0:
            print(0)
        else:
            print(-1)
        return
    else:
        if sum(N) % 3 == 0:
            print(0)
            return
        elif sum(N) % 3 == 1:
            if N.count(1) >= 1:
                print(1)
                return
            elif N.count(4) >= 1:
                print(1)
                return
            elif N.count(7) >= 1:
                print(1)
                return
            elif N.count(2) >= 1 and N.count(5) >= 1:
                print(2)
                return
            elif N.count(2) >= 1 and N.count(8) >= 1:
                print(2)
                return
            elif N.count(5) >= 1 and N.count(8) >= 1:
                print(2)
                return
            elif N.count(2) >= 2:
                print(2)
                return
            elif N.count(5) >= 2:
                print(2)
                return
            elif N.count(8) >= 2:
                print(2)
                return
            elif N.count(3) >= 1 and N.count(6) >= 1:
                print(2)
                return
            elif N.count(3) >= 1 and N.count(9) >= 1:
                print(2)
                return
            elif N.count(6) >= 1 and N.count(9) >= 1:
                print(2)
                return
            elif N.count(3) >= 2:
                print(2)
                return
            elif N.count

if __name__ == '__main__':
    main()