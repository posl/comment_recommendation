def main():
    N, M = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(N)]
    stores.sort()
    ans = 0
    for i in range(N):
        if M <= stores[i][1]:
            ans += stores[i][0] * M
            break
        else:
            ans += stores[i][0] * stores[i][1]
            M -= stores[i][1]
    print(ans)

if __name__ == '__main__':
    main()