def main():
    N = int(input())
    if N == 1:
        print(0)
    elif N == 2:
        print(1)
    else:
        print(N * (N - 1) // 2)
main()

if __name__ == '__main__':
    main()