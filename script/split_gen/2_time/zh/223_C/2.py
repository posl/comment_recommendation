def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    sum = 0
    for i in range(N):
        sum += A[i]/B[i]
    ans = 0
    for i in range(N):
        ans += A[i]*sum/B[i]
    print(ans/2)
solve()
