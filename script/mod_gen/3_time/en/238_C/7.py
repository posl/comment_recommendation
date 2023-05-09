def solve(N):
    MOD = 998244353
    A = []
    while N > 0:
        A.append(N % 10)
        N //= 10
    A.reverse()
    ans = 0
    for i in range(1, len(A)):
        ans += 45 * pow(10, i - 1, MOD) * i
        ans %= MOD
    for i in range(len(A)):
        for j in range(1, A[i]):
            ans += pow(10, len(A) - i - 1, MOD) * (i + 1)
            ans %= MOD
        ans += sum(A[i + 1:]) + 1
        ans %= MOD
    return ans
N = int(input())
print(solve(N))
I got a WA on this problem. I'm not sure if I'm missing something, but I believe my code is correct.
I'm not sure if this is the right place to ask, but I'm having trouble with this problem. I've tried to write a recursive function to solve this, but I'm not sure if it's correct. I'd appreciate any help.
Here's my code:

if __name__ == '__main__':
    solve()