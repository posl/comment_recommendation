def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    S = ""
    while n != 0:
        if n % 2 == 0:
            S = "0" + S
            n //= -2
        else:
            S = "1" + S
            n = (n - 1) // -2
    print(S)

if __name__ == '__main__':
    main()