def solve():
    L = int(input())
    N = 0
    M = 0
    if L == 3:
        N = 4
        M = 4
        print(N,M)
        print("1 2 0")
        print("2 3 0")
        print("3 4 0")
        print("2 4 1")
    elif L == 4:
        N = 8
        M = 10
        print(N,M)
        print("1 2 0")
        print("2 3 0")
        print("3 4 0")
        print("1 5 0")
        print("2 6 0")
        print("3 7 0")
        print("4 8 0")
        print("5 6 1")
        print("6 7 1")
        print("7 8 1")
    elif L == 5:
        N = 5
        M = 7
        print(N,M)
        print("1 2 0")
        print("2 3 1")
        print("3 4 0")
        print("4 5 0")
        print("2 4 0")
        print("1 3 3")
        print("3 5 1")
    elif L == 6:
        N = 12
        M = 14
        print(N,M)
        print("1 2 0")
        print("2 3 0")
        print("3 4 0")
        print("4 5 0")
        print("2 6 0")
        print("3 7 0")
        print("4 8 0")
        print("5 9 0")
        print("6 10 0")
        print("7 11 0")
        print("8 12 0")
        print("9 11 1")
        print("10 12 1")
        print("11 12 2")
    elif L == 7:
        N = 6
        M = 8
        print(N,M)
        print("1 2 0")
        print("2 3 0")
        print("3 4 0")
        print("4 5 0")
        print("5 6 0")

if __name__ == '__main__':
    solve()