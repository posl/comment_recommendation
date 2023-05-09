def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [A[i] - 1 for i in range(N)]
    B = [-1] * N
    B[0] = 0
    now = 0
    for i in range(1, N):
        now = A[now]
        if B[now] == -1:
            B[now] = i
            continue
        loop = i - B[now]
        break
    else:
        loop = N
    now = 0
    K %= loop
    for i in range(K):
        now = A[now]
    print(now + 1)

if __name__ == '__main__':
    main()