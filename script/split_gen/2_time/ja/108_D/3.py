def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N):
        print(i, i + 1, 10 ** 6)
    for i in range(1, N):
        print(i, i + 1, 10 ** 6 - 1)
    for i in range(1, N):
        print(i, i + 1, 10 ** 6 - 2)
    for i in range(1, N):
        print(i, i + 1, 10 ** 6 - 3)
    i = 0
    while i < L - 4:
        print(1, N, 10 ** 6 - 4 - i)
        i += 1
