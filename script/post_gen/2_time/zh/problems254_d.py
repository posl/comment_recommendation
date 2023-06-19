Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n):
    count=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*j==int(i**0.5)**2*j:
                count+=1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    sq = int(N**0.5)
    cnt = 0
    for i in range(1,sq+1):
        for j in range(1,sq+1):
            if i*j <= N:
                cnt += 1
    print(cnt)

=======
Suggestion 3

def is_square(n):
    return n**0.5 == int(n**0.5)

=======
Suggestion 4

def solve():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i * j % 2 == 1:
                ans += 1
    print(ans)

=======
Suggestion 5

def isSquare(n):
    if n < 0:
        return False
    if n == 1:
        return True
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if mid * mid == n:
            return True
        if mid * mid < n:
            low = mid + 1
        else:
            high = mid
    return False

=======
Suggestion 6

def is_square(n):
    return n == int(n**.5)**2

N = int(input())

ans = 0
for i in range(1, N + 1):
    for j in range(i, N + 1):
        if is_square(i * j):
            if i == j:
                ans += 1
            else:
                ans += 2

print(ans)

=======
Suggestion 7

def isSquare(n):
    if n < 0:
        return False
    x = int(n ** 0.5)
    return x * x == n

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*j <= n*n:
                ans += 1
    print(ans)

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
