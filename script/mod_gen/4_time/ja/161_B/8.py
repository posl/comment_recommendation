def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    s = sum(A)
    ans = "Yes"
    for i in range(M):
        if A[i] < s/(4*M):
            ans = "No"
    print(ans)

if __name__ == '__main__':
    solve()