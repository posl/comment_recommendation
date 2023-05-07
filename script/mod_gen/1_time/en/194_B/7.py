def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans = max(ans, min(A[i], B[(i+1)%N]))
    print(ans)

if __name__ == '__main__':
    solve()