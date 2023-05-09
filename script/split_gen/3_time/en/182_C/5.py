def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N = sorted(N)
    if sum(N) % 3 == 0:
        print(0)
        exit()
    elif sum(N) % 3 == 1:
        if len(N) == 1:
            print(-1)
            exit()
        elif 1 in N:
            N.remove(1)
            print(1)
            exit()
        elif 4 in N:
            N.remove(4)
            print(1)
            exit()
        elif 7 in N:
            N.remove(7)
            print(1)
            exit()
        elif len(N) == 2:
            print(-1)
            exit()
        elif 2 in N:
            N.remove(2)
            print(2)
            exit()
        elif 5 in N:
            N.remove(5)
            print(2)
            exit()
        elif 8 in N:
            N.remove(8)
            print(2)
            exit()
        elif len(N) == 3:
            print(-1)
            exit()
        elif 3 in N:
            N.remove(3)
            print(3)
            exit()
        elif 6 in N:
            N.remove(6)
            print(3)
            exit()
        elif 9 in N:
            N.remove(9)
            print(3)
            exit()
        elif len(N) == 4:
            print(-1)
            exit()
        elif 10 in N:
            N.remove(10)
            print(4)
            exit()
        elif 13 in N:
            N.remove(13)
            print(4)
            exit()
        elif 16 in N:
            N.remove(16)
            print(4)
            exit()
        elif len(N) == 5:
            print(-1)
            exit()
        elif 11 in N:
            N.remove(11)
            print(5)
            exit()
        elif 14 in N:
            N.remove(14)
            print(5)
            exit()
        elif 17 in N:
            N.remove(17)
            print(5)
            exit()
        elif len(N) == 6:
            print(-1)
            exit()
        elif 12 in N:
            N.remove(12)
            print(6)
            exit
