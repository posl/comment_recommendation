def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    result = ""
    while N != 0:
        if N % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result
            N -= 1
        N = N // (-2)
    print(result)

if __name__ == '__main__':
    main()