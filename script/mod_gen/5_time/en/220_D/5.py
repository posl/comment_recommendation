def solve(N, A):
    mod = 998244353
    ans = [0] * 10
    ans[A[0]] = 1
    for i in range(1, N):
        new_ans = [0] * 10
        for j in range(10):
            new_ans[(j + A[i]) % 10] += ans[j]
            new_ans[(j * A[i]) % 10] += ans[j]
        for j in range(10):
            new_ans[j] %= mod
        ans = new_ans
    return ans
N = int(input())
A = list(map(int, input().split()))
ans = solve(N, A)
print("\n".join(map(str, ans)))

if __name__ == '__main__':
    solve()