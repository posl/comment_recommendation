def solve():
    # 读取输入
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    # 二分查找
    def binary_search(a, x):
        l = 0
        r = len(a) - 1
        while r - l > 1:
            m = (l + r) // 2
            if a[m] < x:
                l = m
            else:
                r = m
        return l, r
    # 计算最短距离
    def calc(a, b, x):
        l, r = binary_search(a, x)
        res = min(abs(x - a[l]) + abs(a[l] - b[l]),
                  abs(x - a[r]) + abs(a[r] - b[r]),
                  abs(x - b[l]) + abs(a[l] - b[l]),
                  abs(x - b[r]) + abs(a[r] - b[r]))
        return res
    # 计算答案
    for i in range(Q):
        res = min(calc(s, t, x[i]), calc(t, s, x[i]))
        print(res)

if __name__ == '__main__':
    solve()