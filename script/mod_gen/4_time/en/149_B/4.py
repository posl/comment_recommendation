def main():
    a, b, k = map(int, input().split())
    if k <= a:
        a -= k
    else:
        k -= a
        a = 0
        b -= k
        if b < 0:
            b = 0
    print(a, b)

if __name__ == '__main__':
    main()