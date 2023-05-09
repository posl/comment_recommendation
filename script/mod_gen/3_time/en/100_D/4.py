def main():
    N, M = map(int, input().split())
    cake = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2 ** 3):
        cake.sort(key=lambda x: sum([-x[j] if i >> j & 1 else x[j] for j in range(3)]), reverse=True)
        ans = max(ans, sum([sum([cake[j][k] if i >> k & 1 else -cake[j][k] for k in range(3)]) for j in range(M)]))
    print(ans)

if __name__ == '__main__':
    main()