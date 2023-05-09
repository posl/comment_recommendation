def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    #友達リスト
    friends = [[] for _ in range(N)]
    for a, b in AB:
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    #ブロックリスト
    blocks = [[] for _ in range(N)]
    for c, d in CD:
        blocks[c-1].append(d-1)
        blocks[d-1].append(c-1)
    #友達候補
    ans = [0] * N
    for i in range(N):
        cnt = 0
        for j in friends[i]:
            if j in friends[i] and j not in blocks[i]:
                cnt += 1
        ans[i] = len(friends[i]) - cnt
        ans[i] -= 1
    print(*ans)

if __name__ == '__main__':
    main()