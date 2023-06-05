def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # print(a)
    # print(b)
    # 从后往前推
    # 最后一个跳跃
    if x == a[n-1] or x == b[n-1]:
        print('Yes')
        return
    # 倒数第二个跳跃
    if x > a[n-1] and x < b[n-1]:
        print('Yes')
        return
    # 倒数第三个跳跃
    if x > a[n-2] and x < b[n-2]:
        print('Yes')
        return
    # 倒数第四个跳跃
    if x > a[n-3] and x < b[n-3]:
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    main()