def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
        return
    if b == 0:
        print(n)
        return
    print((n // (a+b)) * a + min(a, n % (a+b)))

if __name__ == '__main__':
    main()