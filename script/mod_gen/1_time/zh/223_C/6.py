def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = input().split()
        a.append(int(ai))
        b.append(int(bi))
    # print(a)
    # print(b)
    # 从左到右
    left = 0
    for i in range(n):
        left += a[i]
    # print(left)
    # 从右到左
    right = 0
    for i in range(n):
        right += a[n - 1 - i]
    # print(right)
    # 从左到右
    left_speed = 0
    for i in range(n):
        left_speed += b[i]
    # print(left_speed)
    # 从右到左
    right_speed = 0
    for i in range(n):
        right_speed += b[n - 1 - i]
    # print(right_speed)
    # 两团火焰将在距离物体左端3厘米处相遇。
    # 两个火焰相遇的位置与物体的左端之间的距离
    # 两个火焰相遇的位置与物体的右端之间的距离
    # 两个火焰相遇的时间
    # 两个火焰相遇的位置与物体的左端之间的距离
    # 两个火焰相遇的位置与物体的右端之间的距离
    # 两个火焰相遇的时间
    # 两个火焰相遇的位置与物体的左端之间的距离
    # 两个火焰相遇的位置与物体的右端之间的距离
    # 两个火焰相遇的时间
    # 两个火焰相遇的时间
    t = left / (left_speed + right_speed)
    # print(t)
    # 两个火焰相遇的位置与物体的左端之间的距离
    # 两个火焰相遇

if __name__ == '__main__':
    main()