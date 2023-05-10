def main():
    N = int(input())
    if N % 2 == 0:
        print(N // 2)
    else:
        print((N + 1) // 2)

if __name__ == '__main__':
    main()