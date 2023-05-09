def main():
    N, M, Q = map(int, input().split())
    trains = []
    for i in range(M):
        L, R = map(int, input().split())
        trains.append((L, R))
    queries = []
    for i in range(Q):
        p, q = map(int, input().split())
        queries.append((p, q))
    for p, q in queries:
        ans = 0
        for L, R in trains:
            if p <= L and R <= q:
                ans += 1
        print(ans)
