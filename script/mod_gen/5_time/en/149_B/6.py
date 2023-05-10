def main():
    a, b, k = map(int, input().split())
    if k <= a:
        a -= k
    else:
        a = 0
        k -= a
        if k <= b:
            b -= k
        else:
            b = 0
    print(a, b)

if __name__ == '__main__':
    main()