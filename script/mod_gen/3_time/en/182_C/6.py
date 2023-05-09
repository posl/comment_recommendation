def main():
    N = input()
    N = N[::-1]
    N = [int(s) for s in N]
    Nsum = sum(N)
    if Nsum % 3 == 0:
        print(0)
        return
    if len(N) == 1:
        print(-1)
        return
    if len(N) == 2:
        if Nsum % 3 == 0:
            print(0)
        else:
            print(-1)
        return
    if N[0] % 3 == 0 or N[1] % 3 == 0 or N[2] % 3 == 0:
        print(1)
        return
    if Nsum % 3 == 1:
        if len(N) >= 4 and (N[3] % 3 == 1 or N[3] % 3 == 2):
            print(2)
            return
        if len(N) >= 5 and (N[4] % 3 == 1 or N[4] % 3 == 2):
            print(2)
            return
        if len(N) >= 6 and (N[5] % 3 == 1 or N[5] % 3 == 2):
            print(2)
            return
        if len(N) >= 7 and (N[6] % 3 == 1 or N[6] % 3 == 2):
            print(2)
            return
        if len(N) >= 8 and (N[7] % 3 == 1 or N[7] % 3 == 2):
            print(2)
            return
        if len(N) >= 9 and (N[8] % 3 == 1 or N[8] % 3 == 2):
            print(2)
            return
        if len(N) >= 10 and (N[9] % 3 == 1 or N[9] % 3 == 2):
            print(2)
            return
        if len(N) >= 11 and (N[10] % 3 == 1 or N[10] % 3 == 2):
            print(2)
            return
        if len(N) >= 12 and (N[11] % 3 == 1 or

if __name__ == '__main__':
    main()