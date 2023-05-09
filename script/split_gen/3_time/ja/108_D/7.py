def main():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 1)
        return
    N = 2 * L - 1
    M = N - 1 + N // 2
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N, 2):
        print(i, i + 2, 1)
    for i in range(2, N, 2):
        print(i, i + 2, i // 2)
