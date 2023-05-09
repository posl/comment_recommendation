def main():
    N, K = [int(i) for i in input().split()]
    if N % K == 0:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()