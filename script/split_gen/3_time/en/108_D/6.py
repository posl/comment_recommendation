def main():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 1)
        return
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N - 1):
        print(i, i + 2, 1)
    L -= 2
    for i in range(1, N - 1):
        if L == 0:
            break
        if L >= 2 ** (N - i - 1):
            print(i, i + 2, 2 ** (N - i - 2))
            L -= 2 ** (N - i - 1)
    for i in range(1, N - 1):
        if L == 0:
            break
        if L >= 2 ** (N - i - 1):
            print(i, i + 2, 2 ** (N - i - 2) + 1)
            L -= 2 ** (N - i - 1)
