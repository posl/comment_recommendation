def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            S.add(A[i] + A[j])
    ans = -1
    for i in S:
        if i % D == 0:
            ans = max(ans, i)
    print(ans)
