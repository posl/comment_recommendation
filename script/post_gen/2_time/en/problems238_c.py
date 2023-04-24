Synthesizing 10/10 solutions

=======
Suggestion 1

def   f ( x ): 
     if   x   ==   0 : 
         return   0 
     if   x   <   10 : 
         return   x 
     l   =   len ( str ( x )) 
     return   f ( x   -   10   *   ( 10   **   ( l   -   2 )))   +   ( 10   **   ( l   -   1 ))   *   ( l   -   1 )   *   9   +   10   *   ( l   -   1 )

=======
Suggestion 2

def   f ( x ): 
     if   x   <=   9 : 
         return   x 
     d   =   len ( str ( x )) 
     return   ( 10   **   ( d   -   1 )   -   1 )   +   9   *   ( d   -   1 )   +   f ( x   -   10   **   ( d   -   1 )   +   1 )

=======
Suggestion 3

def f(n, d):
    if n < 10 ** d:
        return n
    else:
        return 9 * 10 ** (d - 1) + f(n - 9 * 10 ** (d - 1), d + 1)

n = int(input())
d = 1
ans = 0
while 10 ** d <= n:
    ans += f(10 ** d - 1, d)
    d += 1
ans += f(n, d)
print(ans % 998244353)

=======
Suggestion 4

def solve(n):
    if n <= 9:
        return n * (n + 1) // 2
    else:
        d = len(str(n))
        ans = 0
        for i in range(1, d):
            ans += i * 9 * (10 ** (i - 1))
        ans += d * (n - (10 ** (d - 1)) + 1)
        return ans

=======
Suggestion 5

def   f ( n ): 
     if   n   <=   9 : 
         return   n 
     else : 
         length   =   len ( str ( n )) 
         ans   =   0 
         for   i   in   range ( 1 ,   length ): 
             ans   +=   9   *   10 ** ( i - 1 )   *   i 
         ans   +=   ( n   -   10 ** ( length - 1 )   +   1 )   *   length 
         return   ans

=======
Suggestion 6

def solve(n):
    if n <= 9:
        return n * (n + 1) // 2
    else:
        s = 0
        for i in range(1, 10):
            s += i * (n // 10 ** i)
        return s + solve(n % 10 ** (len(str(n)) - 1)) + 1

n = int(input())
print(solve(n) % 998244353)

This is a solution for the problem "A - 1, 2, 3, ...". The problem is here. The problem statement is as follows.

Given integers N and M, find the number of ways to choose N integers from 1, 2, ..., M that satisfy the following condition:

The sum of the chosen integers is a multiple of M.

Constraints

N, M are integers.
1 ≦ N ≦ M ≦ 10^9

Input

Input is given from Standard Input in the following format:

N M

Output

Print the answer as an integer.

Sample Input 1

2 5

Sample Output 1

2

There are two ways to choose two integers from 1, 2, 3, 4, 5 that satisfy the condition.

[1, 4]
[2, 3]

Sample Input 2

3 4

Sample Output 2

3

There are three ways to choose three integers from 1, 2, 3, 4 that satisfy the condition.

[1, 1, 2]
[1, 2, 1]
[2, 1, 1]

Sample Input 3

10 100000

Sample Output 3

0

There is no way to choose ten integers from 1, 2, 3, ..., 100000 that satisfy the condition.

=======
Suggestion 7

def f(x):
    if x <= 0:
        return 0
    if x < 10:
        return x
    n = len(str(x))
    return 9 * 10 ** (n - 2) + n * f(x % 10 ** (n - 1)) + f(x // 10)

=======
Suggestion 8

def solve(n):
    ans = 0
    for i in range(1, len(str(n))):
        ans += 9 * i * pow(10, i - 1, 998244353)

    ans %= 998244353
    ans += (n - pow(10, len(str(n)) - 1) + 1) * len(str(n))
    ans %= 998244353
    return ans

=======
Suggestion 9

def f(n):
    if n < 10: return n
    k = len(str(n))
    return 9 * pow(10, k - 2, MOD) + f(n % pow(10, k - 1))

MOD = 998244353
N = int(input())
print((f(N) + f(N + 1)) % MOD)

=======
Suggestion 10

def   main ():
    N  =  int ( input ())
    print ( solve (N))
