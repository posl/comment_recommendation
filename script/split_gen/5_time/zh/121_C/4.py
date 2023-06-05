def main():
    # 读入数据
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    # 按照a从小到大排序
    ab.sort()
    # 从最小的开始买，直到买够m罐
    ans = 0
    for a, b in ab:
        if b < m:
            ans += a * b
            m -= b
        else:
            ans += a * m
            break
    print(ans)
