def main():
    N = int(input())
    P = list(map(int, input().split()))
    if N == 2:
        print(0)
        return
    if N == 3:
        if P[0] == 0 and P[1] == 1 and P[2] == 2:
            print(3)
            return
        else:
            print(2)
            return
    if N == 4:
        if P[0] == 0 and P[1] == 1 and P[2] == 2 and P[3] == 3:
            print(4)
            return
        else:
            print(3)
            return
    if N == 5:
        if P[0] == 0 and P[1] == 1 and P[2] == 2 and P[3] == 3 and P[4] == 4:
            print(5)
            return
        else:
            print(4)
            return
    if N == 6:
        if P[0] == 0 and P[1] == 1 and P[2] == 2 and P[3] == 3 and P[4] == 4 and P[5] == 5:
            print(6)
            return
        else:
            print(5)
            return
    if N == 7:
        if P[0] == 0 and P[1] == 1 and P[2] == 2 and P[3] == 3 and P[4] == 4 and P[5] == 5 and P[6] == 6:
            print(7)
            return
        else:
            print(6)
            return
    if N == 8:
        if P[0] == 0 and P[1] == 1 and P[2] == 2 and P[3] == 3 and P[4] == 4 and P[5] == 5 and P[6] == 6 and P[7] == 7:
            print(8)
            return
        else:
            print(7)
            return
    if N == 9:
        if P[0] == 0 and P[1] == 1 and P[2] == 2 and P

if __name__ == '__main__':
    main()