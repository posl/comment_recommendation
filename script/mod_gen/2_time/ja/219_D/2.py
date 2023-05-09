def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = 300 * 300 + 1
    for i in range(1, 2 ** N):
        a = 0
        b = 0
        cnt = 0
        for j in range(N):
            if i & (1 << j):
                a += A[j]
                b += B[j]
                cnt += 1
        if a >= X and b >= Y:
            ans = min(ans, cnt)
    if ans > 300 * 300:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()