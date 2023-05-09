def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] + A[j] <= 100:
                S.add(A[i] + A[j])
    S = sorted(S, reverse=True)
    for s in S:
        if s % D == 0:
            print(s)
            exit()
    print(-1)
