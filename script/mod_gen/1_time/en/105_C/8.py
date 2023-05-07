def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    res = ""
    while N != 0:
        if N % 2 == 0:
            res += "0"
            N //= -2
        else:
            res += "1"
            N = (N - 1) // -2
    print(res[::-1])

if __name__ == '__main__':
    main()