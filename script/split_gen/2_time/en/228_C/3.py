def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    for p in P:
        p.append(sum(p))
    P.sort(key=lambda x: x[3], reverse=True)
    print(*['Yes' if p[3] >= P[K-1][3] else 'No' for p in P], sep='
')
