def solve():
    # H, W = map(int, input().split())
    # S = [input() for _ in range(H)]
    # cnt = 0
    # for i in range(H):
    #     for j in range(W):
    #         if S[i][j] == '#':
    #             cnt += 1
    # print(cnt)
    print(sum(row.count('#') for row in [input() for _ in range(int(input().split()[0]))]))

if __name__ == '__main__':
    solve()