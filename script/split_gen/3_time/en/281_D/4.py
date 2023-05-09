def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(2**N):
        S.add(sum([A[j] for j in range(N) if ((i>>j) & 1)]))
    S = sorted([s for s in S if s % D == 0])
    if len(S) == 0:
        print(-1)
    else:
        print(S[-1])
