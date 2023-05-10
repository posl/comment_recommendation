def main():
    x = input()
    m = int(input())
    d = int(max(x))
    if len(x) == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
        return
    # 二分探索
    l = d + 1
    r = m + 1
    while r - l > 1:
        mid = (l + r) // 2
        if x2num(x, mid) <= m:
            l = mid
        else:
            r = mid
    print(l - d)

if __name__ == '__main__':
    main()