def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    ans = [1, 1] #初期位置
    for i in range(1000000):
        if ans[0] == H and ans[1] == W:
            break
        if G[ans[0]-1][ans[1]-1] == 'U' and ans[0] != 1:
            ans[0] -= 1
        elif G[ans[0]-1][ans[1]-1] == 'D' and ans[0] != H:
            ans[0] += 1
        elif G[ans[0]-1][ans[1]-1] == 'L' and ans[1] != 1:
            ans[1] -= 1
        elif G[ans[0]-1][ans[1]-1] == 'R' and ans[1] != W:
            ans[1] += 1
        else:
            ans = [-1]
            break
    print(*ans)

if __name__ == '__main__':
    main()