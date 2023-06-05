def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if sum(A) <= N:
        print(N - sum(A))
    else:
        print(-1)

if __name__ == '__main__':
    main()