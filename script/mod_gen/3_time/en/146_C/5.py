def main():
    A, B, X = map(int, input().split())
    # 1桁の場合
    if X < A + B:
        print(0)
        return
    # 10^9桁の場合
    if X >= A * 10**9 + B * 10:
        print(10**9)
        return
    # 1桁から9桁までの場合
    left = 1
    right = 10**9
    while right - left > 1:
        mid = (left + right) // 2
        # A * mid + B * d(mid) <= X
        if A * mid + B * len(str(mid)) <= X:
            left = mid
        else:
            right = mid
    print(left)

if __name__ == '__main__':
    main()