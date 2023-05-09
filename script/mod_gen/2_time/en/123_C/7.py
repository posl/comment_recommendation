def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if n % a == 0:
        ans = n // a
    else:
        ans = n // a + 1
    if n % b == 0:
        ans = max(ans, n // b)
    else:
        ans = max(ans, n // b + 1)
    if n % c == 0:
        ans = max(ans, n // c)
    else:
        ans = max(ans, n // c + 1)
    if n % d == 0:
        ans = max(ans, n // d)
    else:
        ans = max(ans, n // d + 1)
    if n % e == 0:
        ans = max(ans, n // e)
    else:
        ans = max(ans, n // e + 1)
    print(ans + 4)

if __name__ == '__main__':
    main()