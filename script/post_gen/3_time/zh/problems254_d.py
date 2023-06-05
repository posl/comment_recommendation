Synthesizing 10/10 solutions

=======
Suggestion 1

def get_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return divisors

=======
Suggestion 2

def solve(n):
    ans = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i * j <= n and i * i != j * j:
                ans += 2
            elif i * j <= n and i * i == j * j:
                ans += 1
    return ans

=======
Suggestion 3

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 4

def solve(n):
    cnt = 0
    # 1の場合は1通り
    if n == 1:
        return 1
    # 2以上の場合
    for i in range(1, n+1):
        # i**2がnを超えるまで繰り返す
        if i**2 > n:
            break
        # i**2がn以下の場合
        for j in range(i, n+1):
            # i*jがnを超えるまで繰り返す
            if i*j > n:
                break
            # i*jがn以下の場合
            cnt += 1
    return cnt

=======
Suggestion 5

def main():

    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j > N:
                break
            ans += 1
    print(ans)

=======
Suggestion 6

def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

=======
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        for j in range(i,N+1):
            if (i*j)**0.5 == int((i*j)**0.5):
                count += 1
    print(count)

=======
Suggestion 8

def isSquare(n):
    from math import sqrt
    return sqrt(n) == int(sqrt(n))

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if (i*j)**0.5 == int((i*j)**0.5):
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    i = 1
    ans = 0
    while i*i <= n:
        j = 1
        while i*j <= n:
            ans += 1
            j += 1
        i += 1
    print(ans)
