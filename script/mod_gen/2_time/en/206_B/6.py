def main():
    N = int(input())
    l = 0
    r = 10**9 + 1
    while r - l > 1:
        mid = (l + r) // 2
        if mid * (mid + 1) // 2 >= N:
            r = mid
        else:
            l = mid
    print(r)

if __name__ == '__main__':
    main()