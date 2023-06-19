def main():
    N = int(input())
    result = ''
    while N > 0:
        if N % 2 == 0:
            N = N // 2
            result = 'B' + result
        else:
            N -= 1
            result = 'A' + result
    print(result)

if __name__ == '__main__':
    main()