def main():
    L = int(input())
    N = L + 1
    M = 2 * N - 2
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N - 2):
        print(i, i + 2, 1)
    print(N - 2, N, L - 1)
