def main():
    # 读入数据
    n, m = map(int, input().split())
    k = []
    s = []
    for i in range(m):
        k.append(int(input().split()[0]))
        s.append([int(x) for x in input().split()])
    p = [int(x) for x in input().split()]
    # 穷举
    ans = 0
    for i in range(2 ** n):
        # 计算灯泡状态
        light = [0] * m
        for j in range(n):
            if (i >> j) & 1 == 1:
                for l in range(m):
                    if j + 1 in s[l]:
                        light[l] += 1
        # 检查灯泡状态
        ok = True
        for j in range(m):
            if light[j] % 2 != p[j]:
                ok = False
        # 计数
        if ok:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()