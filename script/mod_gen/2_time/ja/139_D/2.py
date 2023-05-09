def main():
    N = int(input())
    if N == 1:
        print(0)
        exit()
    elif N % 2 == 0:
        print(N // 2 - 1)
    else:
        print(N // 2)

if __name__ == '__main__':
    main()