def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    count = [0] * (N + 1)
    for i in range(1, M):
        a, b = bridges[i - 1]
        if count[a] > count[b]:
            a, b = b, a
        ans[i] = ans[i - 1] - count[a]
        count[a] += 1
        count[b] += 1
    ans.reverse()
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()