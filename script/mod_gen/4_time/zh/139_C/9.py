def solve():
    # 从左向右遍历, 用一个变量来记录当前的最大值
    # 从左向右遍历, 如果当前值小于等于最大值, 则计数+1, 并将最大值更新为当前值
    # 如果当前值大于最大值, 则计数清零, 并将最大值更新为当前值
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_h = 0
    for i in range(n):
        if h[i] >= max_h:
            count += 1
            max_h = h[i]
    print(count)
    return 0

if __name__ == '__main__':
    solve()