def main():
    N, M = map(int, input().split())
    if M == 0:
        print(3 ** N)
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    ans = 0
    for i in range(3 ** N):
        flag = True
        for j in range(N):
            for k in range(j + 1, N):
                if (i >> j & 1) == (i >> k & 1) and k in G[j]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()