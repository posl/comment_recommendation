Synthesizing 10/10 solutions

=======
Suggestion 1

def   main (): 
     N   =   int ( input ()) 
     mod   =   998244353 
     ans   =   0 
     for   i   in   range ( len ( str ( N ))): 
         ans   +=   ( N   -   10   **   i   +   1 )   *   ( 10   **   i )   %   mod 
         ans   %=   mod 
     print ( ans )

=======
Suggestion 2

def get_digit(n):
    digit = 0
    while n > 0:
        n //= 10
        digit += 1
    return digit

=======
Suggestion 3

def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    d = 1
    while d <= N:
        ans += (N // d) * (d - 1) + min(max(N % d - d + 1, 0), d)
        d *= 10
        ans %= MOD
    print(ans)

main()

=======
Suggestion 4

def f(x):
    n = len(str(x))
    return (x-10**(n-1)+1)*n

N = int(input())
ans = 0
for i in range(1,10):
    ans += f(min(10**i-1,N))
    if 10**i > N:
        break
print(ans%(998244353))

=======
Suggestion 5

def f(n):
    if n==0:
        return 0
    if n<10:
        return sum(range(1,n+1))
    d=len(str(n))
    ans=0
    for i in range(1,d):
        ans+=45*10**(i-1)*i
    ans+=f(n%10**(d-1))
    ans+=sum(range(1,n//10**(d-1)+1))*d
    return ans

N=int(input())
print(f(N)%998244353)

=======
Suggestion 6

def f(n):
    if n < 10:
        return n
    else:
        l = len(str(n))
        return (9 * (l - 1) * pow(10, l - 2, MOD) + (n - pow(10, l - 1, MOD) + 1)) % MOD

n = int(input())
MOD = 998244353
ans = 0
for i in range(1, len(str(n)) + 1):
    m = pow(10, i, MOD) - 1
    ans += f(m)
    ans %= MOD
ans += f(n)
ans %= MOD
print(ans)

This code is written in Python 3.4.3.

Th

=======
Suggestion 7

def main():
    N = int(input())
    MOD = 998244353
    #dp[i][j] := i桁の数字で、最大値がjのものの個数
    dp = [[0 for j in range(10)] for i in range(19)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, 19):
        for j in range(1, 10):
            for k in range(1, j+1):
                dp[i][j] += dp[i-1][k]
                dp[i][j] %= MOD
    ans = 0
    for i in range(1, 19):
        for j in range(1, 10):
            ans += dp[i][j]
            ans %= MOD
    N += 1
    for i in range(1, 19):
        if N < 10**i:
            break
        for j in range(1, 10):
            ans += dp[i][j]
            ans %= MOD
    s = str(N)
    for i in range(1, len(s)):
        for j in range(1, 10):
            ans += dp[i][j]
            ans %= MOD
    for i in range(1, int(s[0])):
        for j in range(1, 10):
            if i > j:
                continue
            ans += dp[len(s)][j]
            ans %= MOD
    for i in range(1, len(s)):
        for j in range(1, int(s[i])):
            if int(s[i-1]) > j:
                continue
            ans += dp[len(s)-i][j]
            ans %= MOD
    print(ans)

=======
Suggestion 8

def  main():
    N = int(input())
    ans = 0
    for  i in range(1, 19):
         if  N < 10 ** i:
            ans += solve(N, i)
             break 
        ans += solve(10 ** i - 1, i)
    print(ans % 998244353)

=======
Suggestion 9

def   solve ( N ): 
     # 10^{18} 以下の整数 N について、以下の問題を解く。 
     # f(x) = (x 以下の桁数が x と同じ正の整数の個数) 
     # f(1) + f(2) + ... + f(N) を 998244353 で割った余りを求めよ。 
     # 1 ≦ N < 10^{18} 

     # 10^{18} 以下の整数 N について、以下の問題を解く。 
     # f(x) = (x 以下の桁数が x と同じ正の整数の個数) 
     # f(1) + f(2) + ... + f(N) を 998244353 で割った余りを求めよ。 
     # 1 ≦ N < 10^{18} 

     # 10^{18} 以下の整数 N について、以下の問題を解く。 
     # f(x) = (x 以下の桁数が x と同じ正の整数の個数) 
     # f(1) + f(2) + ... + f(N) を 998244353 で割った余りを求めよ。 
     # 1 ≦ N < 10^{18} 

     # 10^{18} 以下の整数 N について、以下の問題を解く。 
     # f(x) = (x 以下の桁数が x と同じ正の整数の個数) 
     # f(1) + f(2) + ... + f(N) を 998244353 で割った余りを求めよ。 
     # 1 ≦ N < 10^{18} 

     # 10^{18} 以下の整数 N について、以下の問題を解く。 
     # f(x) = (x 以下の桁数が x と同じ正の整数の個数)

=======
Suggestion 10

def sum_of_digits(n):
    return sum([int(i) for i in str(n)])
