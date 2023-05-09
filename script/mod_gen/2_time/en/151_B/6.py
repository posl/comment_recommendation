def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    if S >= M*N:
        print(0)
    elif S + K*(N-1) < M*N:
        print(-1)
    else:
        print(max(0, M*N-S))

if __name__ == '__main__':
    main()