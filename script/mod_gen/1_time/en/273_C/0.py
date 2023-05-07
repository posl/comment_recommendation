def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        ans[i] = ans[i-1]
        if A[i] != A[i-1]:
            ans[i] += 1
    ans = ans[::-1]
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    solve()