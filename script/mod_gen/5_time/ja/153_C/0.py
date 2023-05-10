def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    if K >= N:
        print(0)
    else:
        print(sum(H[:N-K]))

if __name__ == '__main__':
    main()