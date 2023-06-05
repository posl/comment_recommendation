def main():
    n = int(input())
    res = ""
    while n != 0:
        if n % 2 == 0:
            res = "0" + res
        else:
            res = "1" + res
            n -= 1
        n //= -2
    if res == "":
        print(0)
    else:
        print(res)

if __name__ == '__main__':
    main()