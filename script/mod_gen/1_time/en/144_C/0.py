def main():
    N = int(input())
    i = 1
    while i * i < N:
        i += 1
    if i * i == N:
        print(2 * i - 2)
    else:
        if N % i == 0:
            print(2 * i - 2)
        else:
            print(2 * i - 1)

if __name__ == '__main__':
    main()