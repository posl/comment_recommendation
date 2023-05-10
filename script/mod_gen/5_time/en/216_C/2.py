def main():
    n = int(input())
    s = ""
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            s = "B" + s
        else:
            n -= 1
            s = "A" + s
    print(s)

if __name__ == '__main__':
    main()