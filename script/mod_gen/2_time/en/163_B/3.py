def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if N < total:
        print(-1)
    else:
        print(N - total)

if __name__ == '__main__':
    main()