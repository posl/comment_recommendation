def main():
    a, b, x = map(int, input().split())
    if a * 10**9 + b * 10 <= x:
        print(10**9)
        return
    if a * 1 + b * 1 > x:
        print(0)
        return
    left = 0
    right = 10**9
    while right - left > 1:
        mid = (left + right) // 2
        if a * mid + b * len(str(mid)) > x:
            right = mid
        else:
            left = mid
    print(left)

if __name__ == '__main__':
    main()