def solve():
    # 读入数据
    N, M = map(int, input().split())
    data = []
    for i in range(N):
        A, B = map(int, input().split())
        data.append((A, B))
    # 按照单价从小到大排序
    data.sort()
    # 依次购买能量饮料
    ans = 0
    rest = M
    for i in range(N):
        # 优先购买单价低的
        if rest >= data[i][1]:
            ans += data[i][0] * data[i][1]
            rest -= data[i][1]
        else:
            ans += data[i][0] * rest
            rest = 0
        if rest == 0:
            break
    print(ans)

if __name__ == '__main__':
    solve()