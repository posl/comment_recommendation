def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M * N - sum(A) > K:
        print(-1)
    else:
        print(max(0, M * N - sum(A)))

if __name__ == '__main__':
    main()