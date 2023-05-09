def main():
    a, b, x = map(int, input().split())
    if a > x:
        print(0)
        return
    if a * 1000000000 + b * 10 <= x:
        print(1000000000)
        return
    left = 0
    right = 1000000000
    while left + 1 < right:
        mid = (left + right) // 2
        if a * mid + b * len(str(mid)) <= x:
            left = mid
        else:
            right = mid
    print(left)

if __name__ == '__main__':
    main()