def main():
    n = int(input())
    if n < 1000:
        print(0)
    else:
        num = 0
        for i in range(1, 16):
            if i == 1:
                num += 0
            elif i == 2:
                num += n - 999
            else:
                num += (n - 10**(3*(i-2)) + 1) * (i - 1)
        print(num)

if __name__ == '__main__':
    main()