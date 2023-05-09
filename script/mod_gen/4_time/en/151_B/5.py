def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    score = 0
    for i in range(N-1):
        score += A[i]
    if score >= M*N:
        print(0)
    elif score + K >= M*N:
        print(M*N - score)
    else:
        print(-1)

if __name__ == '__main__':
    main()