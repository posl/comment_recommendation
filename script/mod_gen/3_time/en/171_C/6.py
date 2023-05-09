def main():
    n = int(input())
    s = ""
    while n > 0:
        n -= 1
        a = n % 26
        s = chr(a+97) + s
        n = n // 26
    print(s)

if __name__ == '__main__':
    main()