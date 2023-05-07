def main():
    N = int(input())
    if N % 2 == 0:
        print(N / (N + 1))
    else:
        print((N + 1) / (N + 1))
main()

if __name__ == '__main__':
    main()