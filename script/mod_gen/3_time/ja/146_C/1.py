def main():
    a, b, x = map(int, input().split())
    def d(n):
        return len(str(n))
    def f(n):
        return a * n + b * d(n)
    left = 0
    right = 10 ** 9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if f(mid) <= x:
            left = mid
        else:
            right = mid
    print(left)

if __name__ == '__main__':
    main()