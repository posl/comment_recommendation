def main():
    N, M = map(int, input().split())
    friend_list = [set() for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        friend_list[a-1].add(b-1)
        friend_list[b-1].add(a-1)
    ans = 0
    for i in range(N):
        if len(friend_list[i]) == 0:
            ans += 1
            continue
        friend_list[i].add(i)
        tmp = {i}
        while len(tmp) > 0:
            tmp2 = set()
            for j in tmp:
                tmp2 = tmp2 | friend_list[j]
            tmp = tmp2 - friend_list[i]
            friend_list[i] = friend_list[i] | tmp2
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()