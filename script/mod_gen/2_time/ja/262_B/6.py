def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            a, b = edges[i]
            c, d = edges[j]
            if len({a, b, c, d}) == 4:
                if (a, b) in edges and (b, c) in edges and (c, a) in edges:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()