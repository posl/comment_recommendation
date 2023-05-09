def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    ans = 0
    for a in range(N):
        for b in edge[a]:
            if a < b:
                for c in edge[b]:
                    if b < c and a in edge[c]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()