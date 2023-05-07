def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    for a in A:
        B[a] += 1
    if B[0] == N:
        print(0)
        return
    for i in range(1, M):
        B[i] += B[i - 1]
    for i in range(M - 1):
        B[i] = B[i + 1] - B[i]
    B[M - 1] = N - B[M - 1]
    ans = 0
    for i in range(M):
        if B[i] > 0:
            ans += min(B[i], B[(i + 1) % M]) * i
    print(ans)
main()

if __name__ == '__main__':
    main()