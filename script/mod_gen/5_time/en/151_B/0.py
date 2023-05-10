def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N*M - sum(A) > K:
        print(-1)
    elif N*M - sum(A) > 0:
        print(N*M - sum(A))
    else:
        print(0)

if __name__ == '__main__':
    main()