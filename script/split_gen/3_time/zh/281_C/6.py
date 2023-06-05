def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T -= 1
    T %= sum(A)
    ans = 0
    while T >= A[ans]:
        T -= A[ans]
        ans += 1
    print(ans + 1, T + 1)
