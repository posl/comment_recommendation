def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 二分法
    def check(x):
        cnt = 0
        for i in range(n):
            if a[i] > x:
                cnt += 1
            else:
                cnt -= 1
        for i in range(n):
            if b[i] > x:
                cnt += 1
            else:
                cnt -= 1
        return cnt >= 0
    left = -1
    right = 10 ** 9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    if right == 10 ** 9 + 1:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    solve()