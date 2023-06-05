def main():
    a,b,k = map(int, input().split())
    if k > a:
        b = b - (k - a)
        a = 0
        if b < 0:
            b = 0
    else:
        a = a - k
    print(a,b)

if __name__ == '__main__':
    main()