def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    S = set()
    for i in range(K):
        for j in range(i+1, N):
            S.add(A[i] + A[j])
    ans = -1
    for s in S:
        if s % D == 0:
            ans = s
    print(ans)
