def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
        return
    elif b == 0:
        print(n)
        return
    elif a + b > n:
        print(n)
        return
    else:
        num_a = n // (a + b)
        num_b = n % (a + b)
        if num_b > a:
            num_b = a
        print(num_a * a + num_b)

if __name__ == '__main__':
    main()