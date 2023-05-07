def solve():
    import sys
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(1)
        sys.exit()
    A.sort()
    ans = [0 for _ in range(N)]
    ans[0] = 1
    for i in range(1, N):
        if A[i] != A[i-1]:
            ans[i] = ans[i-1] + 1
        else:
            ans[i] = ans[i-1]
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    solve()