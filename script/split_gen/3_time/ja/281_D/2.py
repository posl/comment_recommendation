def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    S = set()
    for i in range(K):
        for j in range(i+1, K):
            S.add(A[i]+A[j])
    S = sorted(list(S), reverse=True)
    for s in S:
        if s % D == 0:
            print(s)
            return
    print(-1)
