def main():
    k = int(input())
    num = 0
    while k > 0:
        num += 1
        if num % 10 == 2:
            k -= 1
        num //= 10
    print(num)

if __name__ == '__main__':
    main()