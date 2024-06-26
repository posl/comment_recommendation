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
    sum /= 2
    ans = 0
    for i in range(N):
        sum -= A[i]/B[i]
        if sum < 0:
            ans += A[i] + sum*B[i]
            break
        ans += A[i]
    print(ans)

if __name__ == '__main__':
    solve()