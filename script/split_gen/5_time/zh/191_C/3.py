def main():
    # H,W = map(int, input().split())
    # S = [input() for _ in range(H)]
    H = 5
    W = 5
    S = ['.....', '.###.', '.###.', '.###.', '.....']
    print(H,W,S)
    # x = [i for i in range(H) if S[i].count('#') > 0]
    # y = [i for i in range(W) if ''.join([S[j][i] for j in range(H)]).count('#') > 0]
    # print(x,y)
    # if len(x) < 2 or len(y) < 2:
    #     print(0)
    #     return
    # ans = 0
    # for i in range(len(x) - 1):
    #     for j in range(len(y) - 1):
    #         if S[x[i]][y[j]] == '#' and S[x[i]][y[j + 1]] == '#' and S[x[i + 1]][y[j]] == '#' and S[x[i + 1]][y[j + 1]] == '#':
    #             ans += 1
    # print(ans)
    # return
    x = [i for i in range(H) if S[i].count('#') > 0]
    print(x)
    y = [i for i in range(W) if ''.join([S[j][i] for j in range(H)]).count('#') > 0]
    print(y)
    if len(x) < 2 or len(y) < 2:
        print(0)
        return
    ans = 0
    for i in range(len(x) - 1):
        for j in range(len(y) - 1):
            if S[x[i]][y[j]] == '#' and S[x[i]][y[j + 1]] == '#' and S[x[i + 1]][y[j]] == '#' and S[x[i + 1]][y[j + 1]] == '#':
                ans += 1
    print(ans)
    return
main()
