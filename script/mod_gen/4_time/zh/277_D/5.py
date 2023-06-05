def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * N
    for i in range(N):
        B[i] = A[i] % M
    B.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += B[i]
        else:
            if B[i] != B[i - 1]:
                ans += B[i]
    print(ans)

if __name__ == '__main__':
    main()