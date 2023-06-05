def solve(n, k, p):
    # 用来存放结果
    ans = [0] * n
    # 用来存放牌的顺序
    order = [0] * n
    for i in range(n):
        order[p[i] - 1] = i
    # 用来存放桌面上的牌
    cards = []
    for i in range(n):
        # 从牌堆里拿出一张牌
        x = order[i]
        # 如果桌面上的牌比这张牌小，就把桌面上的牌吃掉
        while cards and cards[-1] < x:
            cards.pop()
        # 如果桌面上有k张牌，就把它们吃掉
        if len(cards) == k:
            for j in range(k):
                ans[cards[-1]] = i + 1
                cards.pop()
        # 把这张牌放到桌面上
        cards.append(x)
    # 把桌面上的牌吃掉
    for i in range(len(cards)):
        ans[cards[-1]] = n
        cards.pop()
    return ans
n, k = map(int, input().split())
p = list(map(int, input().split()))
ans = solve(n, k, p)
for i in range(n):
    print(ans[i])

if __name__ == '__main__':
    solve()