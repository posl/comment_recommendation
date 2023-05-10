Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,a,b = map(int,input().split())
    if n < 2:
        print(0)
        return
    if n == 2:
        print(1)
        return
    if a == 1:
        print(n)
        return
    if b == 1:
        print(n)
        return
    if n <= a:
        print(0)
        return
    if n <= b:
        print(0)
        return
    if a == 2:
        print(n-1)
        return
    if b == 2:
        print(n-1)
        return
    if a < b:
        print(n-a)
        return
    if b < a:
        print(n-b)
        return
    print(0)
    return

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if n <= b:
        print(0)
        return
    if a == b:
        print(1)
        return

    comb = 1
    for i in range(n):
        comb *= (n - i)
        comb %= 1000000007
    for i in range(n - b):
        comb *= pow(i + 1, 1000000005, 1000000007)
        comb %= 1000000007
    for i in range(n - a):
        comb *= pow(i + 1, 1000000005, 1000000007)
        comb %= 1000000007
    print((pow(2, n, 1000000007) - comb - comb) % 1000000007)

=======
Suggestion 3

def main():
    n,a,b = map(int,input().split())
    MOD = 10**9 + 7
    ans = pow(2,n,MOD) - 1
    for i in range(b):
        ans = ans * (n-i) % MOD
    for i in range(b):
        ans = ans * pow(i+1,MOD-2,MOD) % MOD
    for i in range(a):
        ans = ans * (n-i) % MOD
    for i in range(a):
        ans = ans * pow(i+1,MOD-2,MOD) % MOD
    print(ans)

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    if a == 1:
        print(0)
        return
    if b == 2:
        print(0)
        return
    if n < b:
        print(0)
        return
    if n == a:
        print(0)
        return
    if n == b:
        print(0)
        return
    if n == a+1 and n == b+1:
        print(0)
        return
    if n == a+1 and n != b+1:
        print(1)
        return
    if n == b+1 and n != a+1:
        print(1)
        return
    if n == a+2 and n == b+2:
        print(1)
        return
    if n == a+2 and n != b+2:
        print(2)
        return
    if n == b+2 and n != a+2:
        print(2)
        return
    if n == a+3 and n == b+3:
        print(2)
        return
    if n == a+3 and n != b+3:
        print(3)
        return
    if n == b+3 and n != a+3:
        print(3)
        return
    if n == a+4 and n == b+4:
        print(3)
        return
    if n == a+4 and n != b+4:
        print(4)
        return
    if n == b+4 and n != a+4:
        print(4)
        return
    if n == a+5 and n == b+5:
        print(4)
        return
    if n == a+5 and n != b+5:
        print(5)
        return
    if n == b+5 and n != a+5:
        print(5)
        return
    if n == a+6 and n == b+6:
        print(5)
        return
    if n == a+6 and n != b+6:
        print(6)
        return
    if n == b+6 and n != a+6:
        print(6)
        return
    if n == a+7 and n == b+7:
        print

=======
Suggestion 5

def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    ans = pow(2, n, mod) - 1
    for i in range(a):
        ans -= comb(n, i, mod)
    for i in range(b):
        ans -= comb(n, i, mod)
    print(ans % mod)

=======
Suggestion 6

def main():
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if b - a == 1:
        print((n - a) * (n - b) % (10**9 + 7))
    else:
        print((n - a) * (n - b) * (n - b - 1) % (10**9 + 7))

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    if b - a == 1:
        print((pow(2, n, mod) - 1) % mod)
    else:
        print((pow(2, n, mod) - 1 - comb(n, a) - comb(n, b)) % mod)

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    if n < b:
        print(0)
    elif a == b:
        print(1)
    else:
        # nCkを求める
        # nCk = n! / k! / (n-k)!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) * (n-k)! / k! / (n-k)!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k * (k-1) * (k-2) * ... * 1
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k * (k-1) * (k-2) * ... * 1
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k * (k-1) * (k-2) * ... * 1
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k * (k-1) * (k-2) * ... * 1
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k!
        # nCk = n * (n-1) * (n-2) * ... * (n-k+1) / k

=======
Suggestion 9

def main():
    n, a, b = map(int, input().split(" "))
    ans = pow(2, n, 10**9 + 7) - 1
    for i in range(n - a, n - b):
        ans -= pow(2, i, 10**9 + 7)
    print(ans % (10**9 + 7))

=======
Suggestion 10

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n,a,b = map(int,input().split())
div = make_divisors(n)
div.sort()
#print(div)
ans = 0
for i in range(len(div)):
    if div[i] == a or div[i] == b:
        continue
    else:
        ans += 1
print(ans)
