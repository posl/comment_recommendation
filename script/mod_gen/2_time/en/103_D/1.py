def main():
    N, M = map(int, input().split())
    bridges = [set() for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        bridges[a].add(b)
        bridges[b].add(a)
    ans = 0
    for i in range(1, N + 1):
        if bridges[i]:
            ans += 1
            for j in bridges[i]:
                bridges[j].discard(i)
    print(ans)

if __name__ == '__main__':
    main()