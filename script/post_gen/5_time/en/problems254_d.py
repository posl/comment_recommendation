Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j > n:
                break
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if (i * j) ** 0.5 % 1 == 0:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (i * j) ** 0.5 == int((i * j) ** 0.5):
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j > n:
                break
            else:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j > N:
                break
            else:
                ans += 1
    print(ans)

=======
Suggestion 6

def divisors(n):
    l = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            l.append(i)
            if i != n // i:
                l.append(n//i)
    return l

n = int(input())
ans = 0
for i in range(1,n+1):
    if i % 2 == 1:
        if len(divisors(i)) == 8:
            ans += 1
print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i*j)**(1/2) == int((i*j)**(1/2)):
                count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j <= n and i * j == int(i * j) ** 2:
                ans += 1
    print(ans)

=======
Suggestion 9

def is_square(n):
    return n == int(n**.5)**2

n = int(input())
ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if is_square(i*j):
            ans += 1
print(ans)

=======
Suggestion 10

def problem():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i*j <= n and i != j:
                cnt += 2
            elif i*j <= n and i == j:
                cnt += 1
    print(cnt)
