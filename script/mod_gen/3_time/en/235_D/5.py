def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
        return
    if a == 2:
        print(n.bit_length())
        return
    count = 0
    while n > 1:
        if n % a == 0:
            n //= a
        elif n % 10 == 1:
            n //= 10
        else:
            print(-1)
            return
        count += 1
    print(count)

if __name__ == '__main__':
    main()