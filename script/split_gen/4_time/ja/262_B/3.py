def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if [i+1, j+1] in edges and [j+1, k+1] in edges and [k+1, i+1] in edges:
                    ans += 1
    print(ans)
