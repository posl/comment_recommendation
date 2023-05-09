def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
        print(i, i + 1, 1)
    for i in range(N - 1):
        print(i + 1, i + 2, (L - 1) - i)
    for i in range(N - 1):
        print(i + 1, i + 2, (L - 1) + i)
