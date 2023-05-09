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
    l = d
    r = m + 1
    while r - l > 1:
        mid = (l + r) // 2
        v = 0
        for i in range(len(x)):
            v = v * mid + int(x[i])
            if v > m:
                break
        if v <= m:
            l = mid
        else:
            r = mid
    print(l - d)
main()

if __name__ == '__main__':
    main()