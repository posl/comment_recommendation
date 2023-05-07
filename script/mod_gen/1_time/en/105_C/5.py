def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    s = ""
    while N != 0:
        if N % 2 == 0:
            s += "0"
            N //= -2
        else:
            s += "1"
            N = (N - 1) // -2
    print(s[::-1])

if __name__ == '__main__':
    main()