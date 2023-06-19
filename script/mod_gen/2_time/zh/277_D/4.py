def problem277_d():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0 for i in range(M)]
    for i in range(N):
        B[A[i]] += 1
    ans = 0
    for i in range(M):
        if B[i] == 0:
            continue
        if B[i] % 2 == 0:
            ans += B[i] * i
        else:
            ans += (B[i] - 1) * i
            B[i + 1] += 1
    print(ans)

if __name__ == '__main__':
    problem277_d()