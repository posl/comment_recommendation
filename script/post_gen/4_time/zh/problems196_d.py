Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W, A, B = map(int, input().split())
    print(solve(H, W, A, B))

=======
Suggestion 2

def f(m,n):
    if m==0:
        return 1
    if m<0 or n==0:
        return 0
    return f(m,n-1)+f(m-n,n)
H,W,A,B=map(int,input().split())
print(f(H*W-A*2-B,B))

=======
Suggestion 3

def main():
    h, w, a, b = map(int, input().split())
    print(int(1))

=======
Suggestion 4

def dfs(i, j, a, b, h, w):
    #print(i, j, a, b)
    if i == h:
        return dfs(0, j + 1, a, b, h, w)
    if j == w:
        return 1
    if a == 0 and b == 0:
        return 0
    if j == w - 1:
        return dfs(i + 1, j, a - 1, b, h, w)
    else:
        return dfs(i + 1, j, a - 1, b, h, w) + dfs(i, j + 2, a, b - 1, h, w)

=======
Suggestion 5

def solve():
    H, W, A, B = map(int, input().split())
    MOD = 10 ** 9 + 7

    fact = [1] * (H + W + 1)
    for i in range(1, H + W + 1):
        fact[i] = fact[i - 1] * i % MOD

    def inv(x):
        return pow(x, MOD - 2, MOD)

    def comb(n, r):
        return fact[n] * inv(fact[n - r]) * inv(fact[r]) % MOD

    ans = 0
    for i in range(B + 1):
        ans += comb(H - A + i - 1, i) * comb(A + W - i - 2, A - 1)
        ans %= MOD

    print(ans)

solve()

=======
Suggestion 6

def f(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return f(x-1) + f(x-2)

=======
Suggestion 7

def cal(a,b):
    if a == 0:
        return 1
    elif a == 1:
        return b
    elif a > b:
        return 0
    else:
        return cal(a,b-1) + cal(a-1,b-1)
    
h,w,a,b = map(int,input().split())
print(cal(a,b)*cal(a,h-b)*cal(w-a,b)*cal(w-a,h-b))

=======
Suggestion 8

def solve():
    pass

=======
Suggestion 9

def solve(h, w, a, b):
    if a == 0:
        return 1
    elif a < 0:
        return 0
    elif h == 0 or w == 0:
        return 0
    else:
        return solve(h - 1, w, a - 2, b) + solve(h, w - 1, a - 1, b) + solve(h - 2, w, a - 2, b) + solve(h, w - 2, a - 2, b)

h, w, a, b = map(int, input().split())
print(solve(h, w, a, b))
