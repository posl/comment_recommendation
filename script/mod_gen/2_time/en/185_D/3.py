def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [A[0] - 1]
    for i in range(1, M):
        B.append(A[i] - A[i - 1] - 1)
    B.append(N - A[M - 1])
    if M == 0:
        print(1)
        return
    k = min(B)
    if k <= 0:
        print(M)
        return
    ans = M
    for b in B:
        ans += b // k
        if b % k == 0:
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()