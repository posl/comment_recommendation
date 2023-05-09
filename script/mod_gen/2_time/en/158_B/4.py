def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
        return
    if b == 0:
        print(n // (a+b) * a)
        return
    if a + b > n:
        print(min(a, n))
        return
    if a + b == n:
        print(a)
        return
    if n % (a+b) <= a:
        print((n // (a+b)) * a + n % (a+b))
    else:
        print((n // (a+b)) * a + a)
main()

if __name__ == '__main__':
    main()