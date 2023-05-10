def main():
    a, b, x = map(int, input().split())
    l = 0
    r = 1000000001
    while(r - l > 1):
        m = (l + r) // 2
        if(a * m + b * len(str(m)) > x):
            r = m
        else:
            l = m
    print(l)

if __name__ == '__main__':
    main()