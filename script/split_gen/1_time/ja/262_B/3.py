def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(M)]
    ans = 0
    for a in range(1, N-1):
        for b in range(a+1, N):
            for c in range(b+1, N+1):
                if [a, b] in edges and [b, c] in edges and [c, a] in edges:
                    ans += 1
    print(ans)
