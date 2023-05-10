def main():
    L = int(input())
    N = 0
    M = 0
    if L == 3:
        N = 5
        M = 5
        print(N, M)
        print("1 2 0")
        print("2 3 1")
        print("3 4 0")
        print("4 5 0")
        print("2 4 0")
        print("1 3 3")
        print("3 5 1")
    else:
        N = L + 1
        M = 2 * L - 1
        print(N, M)
        for i in range(1, L):
            print(i, i + 1, 0)
            print(i, i + 1, 2 ** (i - 1))
        for i in range(1, L):
            print(i, i + 1, L - 1)
