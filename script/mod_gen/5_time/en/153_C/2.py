def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    if K >= N:
        print(0)
    else:
        print(sum(H[K:]))

if __name__ == '__main__':
    main()