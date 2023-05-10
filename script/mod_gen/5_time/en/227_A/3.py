def main():
    # input
    N, K, A = map(int, input().split())
    # compute
    # output
    if K < N:
        print(K)
    else:
        print(K % N)

if __name__ == '__main__':
    main()