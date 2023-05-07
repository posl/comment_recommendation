def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [[0] * N for _ in range(K)]
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(K):
            if i+1 in A[j]:
                ans += 1
                break
    print(N - ans)
