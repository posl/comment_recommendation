def main():
    #write code here
    n = int(input())
    s = ''
    while n > 0:
        n -= 1
        s += chr(n % 26 + 97)
        n //= 26
    print(s[::-1])

if __name__ == '__main__':
    main()