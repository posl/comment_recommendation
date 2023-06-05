def main():
    # 读取数据
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    # 计算
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += a[i][j] * b[j]
        tmp += c
        if tmp > 0:
            ans += 1
    # 输出结果
    print(ans)
