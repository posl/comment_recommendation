Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    return len(str(x))

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += f(i)
print(ans % 998244353)

=======
Suggestion 2

def f(x):
    return len(str(x))

N = int(input())
ans = 0
for i in range(1, N+1):
    ans += f(i)
print(ans%998244353)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) == len(str(N)):
            ans += 1
    print(ans % 998244353)
main()

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += len(str(i))
    print(ans % 998244353)

=======
Suggestion 5

def solve(n):
    ans = 0
    i = 1
    while i <= n:
        ans += n // i
        i *= 10
    return ans

n = int(input())
print(solve(n) % 998244353)

=======
Suggestion 6

def f(x):
    if x < 10:
        return x
    else:
        return 1 + f(x // 10)

=======
Suggestion 7

def solve():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, N+1):
        ans += len(str(i))
    print(ans%MOD)

=======
Suggestion 8

def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    N_first = int(N_str[0])
    N_last = int(N_str[-1])
    N_mid = int(N_str[1:-1]) if N_len > 2 else 0
    #print(N, N_len, N_first, N_mid, N_last)
    if N_len == 1:
        print(N)
    elif N_len == 2:
        print(N_first + (N_last - 1) * 2)
    else:
        print(N_first + (N_mid - 1) * 2 + 9 * (N_len - 2) * (N_mid + 1) + N_last)
