def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    ans = [1, 1]
    for i in range(H*W):
        if G[ans[0]-1][ans[1]-1] == "U":
            ans[0] -= 1
        elif G[ans[0]-1][ans[1]-1] == "D":
            ans[0] += 1
        elif G[ans[0]-1][ans[1]-1] == "L":
            ans[1] -= 1
        elif G[ans[0]-1][ans[1]-1] == "R":
            ans[1] += 1
        if ans[0] == 0 or ans[0] == H+1 or ans[1] == 0 or ans[1] == W+1:
            break
    if ans[0] == 0 or ans[0] == H+1 or ans[1] == 0 or ans[1] == W+1:
        print(" ".join(map(str, ans)))
    else:
        print(-1)

if __name__ == '__main__':
    main()