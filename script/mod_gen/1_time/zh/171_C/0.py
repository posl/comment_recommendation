def main():
    num = int(input())
    res = ""
    while num > 0:
        num -= 1
        res = chr(ord('a') + num % 26) + res
        num //= 26
    print(res)

if __name__ == '__main__':
    main()