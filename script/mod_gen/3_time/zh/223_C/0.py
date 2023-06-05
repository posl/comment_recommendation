def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # print(a)
    # print(b)
    # 两个火焰相遇的时间
    t = sum(a) / sum(b)
    # print(t)
    # 两个火焰相遇的位置
    x = 0
    for i in range(n):
        x += a[i] / b[i]
        if x >= t / 2:
            break
    # print(x)
    # 相遇的位置与物体左端之间的距离
    y = 0
    for i in range(n):
        y += a[i]
        if y >= x * b[i]:
            break
    print(y)

if __name__ == '__main__':
    main()