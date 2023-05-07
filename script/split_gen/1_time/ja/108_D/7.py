def main():
    L = int(input())
    if L % 2 == 0:
        N = 2 * L
        M = 3 * L
        print(N, M)
        for i in range(1, L + 1):
            print(i, i + L, 0)
            print(i, i + L, 1)
            print(i, i + L, 2)
    else:
        N = 2 * L + 1
        M = 3 * L + 1
        print(N, M)
        for i in range(1, L + 1):
            print(i, i + L, 0)
            print(i, i + L, 1)
            print(i, i + L, 2)
        print(1, N, 0)
