def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 二分探索
    left = 0
    right = 10 ** 5 + 1
    while right - left > 1:
        mid = (left + right) // 2
        # 二分探索の条件
        if is_ok(a, mid):
            right = mid
        else:
            left = mid
    print(right)

if __name__ == '__main__':
    main()