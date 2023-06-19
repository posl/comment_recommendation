def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        for j in range(i, N):
            if A[i] < A[j]:
                ans[i] += 1
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    solve()