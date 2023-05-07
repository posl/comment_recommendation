def main():
    N, M = map(int, input().split())
    A = [0] * M
    for i in range(M):
        k = int(input())
        A[i] = [int(x) for x in input().split()]
    cnt = [0] * (N + 1)
    for i in range(M):
        for j in range(k):
            cnt[A[i][j]] += 1
    for i in range(1, N + 1):
        if cnt[i] % 2 == 1:
            print("No")
            return
    print("Yes")
    return
