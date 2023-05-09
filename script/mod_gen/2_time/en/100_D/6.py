def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, 2**3):
        tmp = 0
        for j in range(N):
            tmp += sum([cake[j][k] if (i >> k) & 1 else -cake[j][k] for k in range(3)])
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()