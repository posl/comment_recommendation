def main():
    A, B = map(int, input().split())
    if A <= B:
        print(A)
    else:
        lo = 0
        hi = 10 ** 9
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if mid * (mid + 1) // 2 <= A // B:
                lo = mid
            else:
                hi = mid
        ans = hi + (A - B * hi * (hi + 1) // 2) ** 0.5
        print(ans)

if __name__ == '__main__':
    main()