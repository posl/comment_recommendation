def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    if N % 2 == 0:
        print(N - 1)
    else:
        print(N + 1)

if __name__ == '__main__':
    main()