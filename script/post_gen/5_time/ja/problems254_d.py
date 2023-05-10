Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j > n:
                break
            if (i * j) ** 0.5 == int((i * j) ** 0.5):
                ans += 1
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j > N:
                break
            if (i * j) ** 0.5 == int((i * j) ** 0.5):
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        for j in range(1, int(n ** 0.5) + 1):
            if i * j <= n:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i * j > N:
                break
            if (i * j) ** 0.5 == int((i * j) ** 0.5):
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i*j <= N:
                if (i*j)**0.5 == int((i*j)**0.5):
                    ans += 1
            else:
                break
    print(ans)

=======
Suggestion 6

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

n = int(input())
ans = 0
for i in range(1, n+1):
    divs = get_divisors(i)
    for div in divs:
        if div**2 <= i:
            ans += 1
print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j <= n:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    sq = []
    for i in range(1, int(n ** 0.5) + 1):
        sq.append(i ** 2)
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j in sq:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j <= n and i == j and i * j == int((i * j)**0.5)**2:
                ans += 1
            elif i * j <= n and i * j == int((i * j)**0.5)**2:
                ans += 2
    print(ans)
