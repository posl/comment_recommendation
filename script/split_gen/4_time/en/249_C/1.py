def main():
    from itertools import combinations
    N, K = map(int, input().split())
    S = [set(input()) for _ in range(N)]
    ans = 0
    for comb in combinations(range(N), K):
        ans = max(ans, len(set().union(*[S[i] for i in comb])))
    print(ans)
