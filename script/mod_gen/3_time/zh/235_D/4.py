def main():
    a,n = map(int,raw_input().split())
    count = 0
    while n > 1:
        if n % a == 0:
            n = n / a
        else:
            n -= 1
        count += 1
    print count

if __name__ == '__main__':
    main()