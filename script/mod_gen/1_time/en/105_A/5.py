def main():
    # input
    N, K = map(int, input().split())
    # compute
    # output
    print(0 if N%K==0 else 1)

if __name__ == '__main__':
    main()