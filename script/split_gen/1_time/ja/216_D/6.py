def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        k = int(input())
        A.append(list(map(int, input().split())))
    cnt = [0] * N
    for i in range(M):
        for j in range(k):
            cnt[A[i][j]-1] += 1
    for i in range(N):
        if cnt[i] % 2 == 1:
            print('No')
            return
    print('Yes')
