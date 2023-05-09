def main():
    N, M = map(int, input().split())
    G = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        G[A-1].append(B-1)
        G[B-1].append(A-1)
    ans = 0
    for i in range(3**N):
        col = [i//(3**j)%3 for j in range(N)]
        if all(col[x] != col[y] for x, y in G):
            ans += 1
    print(ans)
