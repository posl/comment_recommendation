def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    res = 0
    if a % 10 != 0:
        res = max(res, a + 10 - a % 10)
    else:
        res = max(res, a)
    if b % 10 != 0:
        res = max(res, b + 10 - b % 10)
    else:
        res = max(res, b)
    if c % 10 != 0:
        res = max(res, c + 10 - c % 10)
    else:
        res = max(res, c)
    if d % 10 != 0:
        res = max(res, d + 10 - d % 10)
    else:
        res = max(res, d)
    if e % 10 != 0:
        res = max(res, e + 10 - e % 10)
    else:
        res = max(res, e)
    print(res)

if __name__ == '__main__':
    main()