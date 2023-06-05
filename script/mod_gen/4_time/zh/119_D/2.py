def solve():
    # 1. 读取输入
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    # 2. 为了计算方便，将所有的值都加上一个哨兵，使得所有的值都是正数
    s = [float('-inf')] + s + [float('inf')]
    t = [float('-inf')] + t + [float('inf')]
    # 3. 对于每一个查询，找到最近的神社和寺庙
    # 3.1. 对于每一个查询，找到最近的神社和寺庙
    for i in range(Q):
        # 3.1.1. 二分查找最近的神社
        left, right = 0, A + 1
        while left < right:
            mid = (left + right) // 2
            if s[mid] > x[i]:
                right = mid
            else:
                left = mid + 1
        # left - 1就是最近的神社
        shrine = s[left - 1]
        # 3.1.2. 二分查找最近的寺庙
        left, right = 0, B + 1
        while left < right:
            mid = (left + right) // 2
            if t[mid] > x[i]:
                right = mid
            else:
                left = mid + 1
        # left - 1就是最近的寺庙
        temple = t[left - 1]
        # 3.1.3. 计算最近的神社和寺庙之间的距离
        dist1 = abs(shrine - x[i])
        dist2 = abs(temple - x[i])
        dist3 = abs(shrine - temple) + min(dist1, dist2)
        # 3.1.4. 打印答案
        print(min(dist1, dist2, dist3))
if

if __name__ == '__main__':
    solve()