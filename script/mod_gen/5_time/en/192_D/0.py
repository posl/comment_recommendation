def main():
    x = input()
    m = int(input())
    d = int(max(x))
    if len(x) == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
    else:
        l = d + 1
        r = m + 1
        if l == r:
            print(1)
        else:
            while r - l > 1:
                mid = (l + r) // 2
                val = 0
                for i in range(len(x)):
                    val += int(x[len(x) - i - 1]) * (mid ** i)
                if val <= m:
                    l = mid
                else:
                    r = mid
            print(l - d)

if __name__ == '__main__':
    main()