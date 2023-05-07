def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    # print(G)
    # print(H, W)
    ans = []
    ans.append([1, 1])
    i = 0
    while True:
        # print(ans[i])
        if G[ans[i][0] - 1][ans[i][1] - 1] == "U":
            if ans[i][0] == 1:
                break
            else:
                ans.append([ans[i][0] - 1, ans[i][1]])
        elif G[ans[i][0] - 1][ans[i][1] - 1] == "D":
            if ans[i][0] == H:
                break
            else:
                ans.append([ans[i][0] + 1, ans[i][1]])
        elif G[ans[i][0] - 1][ans[i][1] - 1] == "L":
            if ans[i][1] == 1:
                break
            else:
                ans.append([ans[i][0], ans[i][1] - 1])
        elif G[ans[i][0] - 1][ans[i][1] - 1] == "R":
            if ans[i][1] == W:
                break
            else:
                ans.append([ans[i][0], ans[i][1] + 1])
        i += 1
        if i >= len(ans):
            break
    # print(ans)
    if i == len(ans):
        print(-1)
    else:
        print(" ".join(map(str, ans[-1])))
