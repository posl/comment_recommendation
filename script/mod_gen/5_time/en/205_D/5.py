def solve(N, Q, A, K):
    # write your code here
    return 0
N, Q = map(int, input().split())
A = list(map(int, input().split()))
K = [int(input()) for i in range(Q)]
ans = solve(N, Q, A, K)
for i in ans:
    print(i)

if __name__ == '__main__':
    solve()