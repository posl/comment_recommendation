def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(K):
        S |= {sum(A[j] for j in comb) for comb in combinations(range(N), i+1)}
    S = [s for s in S if s % D == 0]
    print(max(S) if S else -1)
