def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    #print(a, b)
    #print(max(a), max(b))
    #print(min(a), min(b))
    # 1. 生成一个列表，记录每一天有多少人登录
    # 2. 从中找出有k个人登录的天数
    # 3. 输出
    # 1.
    c = [0] * (max(a) + max(b) + 1)
    for i in range(n):
        for j in range(a[i], a[i] + b[i]):
            c[j] += 1
    #print(c)
    # 2.
    d = [0] * (n + 1)
    for i in range(len(c)):
        if c[i] > 0:
            d[c[i]] += 1
    #print(d)
    # 3.
    for i in range(1, n + 1):
        print(d[i], end=' ')
    print()

if __name__ == '__main__':
    main()