def main():
    n, a, b = map(int, input().split())
    if n < a or n < b:
        print(0)
        return
    if a + b > n:
        print(0)
        return
    if a == b:
        print(1)
        return
    if a > n/2:
        a = n - a
    if b > n/2:
        b = n - b
    if a == 1:
        print(n)
        return
    if b % a == 0:
        print(2)
        return
    if a == 2:
        print(n - b)
        return
    if b % a == 1:
        print(2)
        return
    print(1)

if __name__ == '__main__':
    main()