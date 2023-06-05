def solve():
    # 读入数据
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # 按照高桥能得到的票数排序
    AB.sort(key=lambda x: 2 * x[0] + x[1], reverse=True)
    # 高桥得到的票数
    total = sum([x[0] for x in AB])
    # 需要发表演讲的镇数
    cnt = 0
    # 直到高桥得到的票数超过青木的票数
    for i in range(N):
        total -= AB[i][0] + AB[i][1]
        cnt += 1
        if total < 0:
            break
    print(cnt)

if __name__ == '__main__':
    solve()