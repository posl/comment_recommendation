def main():
    N, M = map(int, input().split())
    k = [int(input()) for _ in range(M)]
    a = [list(map(int, input().split())) for _ in range(M)]
    count = [0] * N
    for i in range(M):
        for j in range(k[i]):
            count[a[i][j] - 1] += 1
    for i in range(N):
        if count[i] % 2 == 1:
            print("No")
            return
    print("Yes")
