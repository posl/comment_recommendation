def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(N * (N-1) // 2)

if __name__ == '__main__':
    main()