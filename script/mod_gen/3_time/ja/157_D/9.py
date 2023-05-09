def main():
    N, M, K = map(int, input().split())
    #友達関係
    friend = {}
    for i in range(M):
        a, b = map(int, input().split())
        if a in friend:
            friend[a].append(b)
        else:
            friend[a] = [b]
        if b in friend:
            friend[b].append(a)
        else:
            friend[b] = [a]
    #ブロック関係
    block = {}
    for i in range(K):
        c, d = map(int, input().split())
        if c in block:
            block[c].append(d)
        else:
            block[c] = [d]
        if d in block:
            block[d].append(c)
        else:
            block[d] = [c]
    #友達候補
    ans = [0] * N
    for i in range(N):
        ans[i] = N - 1
        if i + 1 in friend:
            ans[i] -= len(friend[i + 1])
        if i + 1 in block:
            for j in block[i + 1]:
                if j in friend:
                    if i + 1 in friend[j]:
                        ans[i] -= 1
    print(*ans)

if __name__ == '__main__':
    main()