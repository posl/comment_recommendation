def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [0] * K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    ans = 0
    for i in range(1, N + 1):
        for j in range(K):
            if i in A[j]:
                break
            if j == K - 1:
                ans += 1
    print(ans)
