Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, i+1):
            if i * j > N:
                break
            if i == j:
                ans += 1
            elif (i * j) ** 0.5 == int((i * j) ** 0.5):
                ans += 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j <= N:
                if (i*j)**0.5 == int((i*j)**0.5):
                    ans += 1
            else:
                break
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i*j <= N and (i*j)**(1/2) % 1 == 0:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i*j <= n and i == j:
                ans += 1
            elif i*j <= n and i != j:
                ans += 2
    print(ans)

=======
Suggestion 5

def is_square(n):
    return n == int(n**.5)**2

N = int(input())
ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if is_square(i*j):
            ans += 1
print(ans)

=======
Suggestion 6

def solve():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i*j <= n and (i*j)**0.5 == int((i*j)**0.5):
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        for j in range(i,N+1):
            if i*j <= N:
                if (i*j)**0.5 == int((i*j)**0.5):
                    count += 1
            else:
                break
    print(count)

=======
Suggestion 8

def is_square(n):
    return n**.5 == int(n**.5)

n = int(input())

ans = 0
for i in range(1,n+1):
    for j in range(i,n+1):
        if is_square(i*j):
            if i == j:
                ans += 1
            else:
                ans += 2

print(ans)

=======
Suggestion 9

def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    if n % 2 == 1:
        return False
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y:
            return False
        y.add(x)
    return True

n = int(input())
ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if is_square(i*j):
            ans += 1
print(ans)

=======
Suggestion 10

def is_square(n):
    return int(n**0.5)**2 == n
