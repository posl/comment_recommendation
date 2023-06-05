def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] //= 2
    LCM = 1
    for i in range(N):
        LCM = LCM * A[i] // gcd(LCM, A[i])
    LCM *= 2
    ans = M // LCM
    return ans

if __name__ == '__main__':
    solve()