Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    for a in range(1, N):
        for b in range(1, N):
            c = N - a * b
            if c > 0:
                count += 1
            else:
                break
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        ans += (N - 1) // i
    print(ans)

=======
Suggestion 3

def get_divisors(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num%i == 0:
            divisors.append(i)
            if num//i != i:
                divisors.append(num//i)
    return divisors

N = int(input())
divisors = get_divisors(N)
ans = 0
for i in divisors:
    if i == 1:
        continue
    if (N - i) % i == 0:
        ans += (N - i) // i
print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j >= n:
                break
            if i * j < n:
                ans += 1
    print(ans)

=======
Suggestion 5

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

n = int(input())
divisors = get_divisors(n)
ans = 0

for a in divisors:
    m = n // a - 1
    if m > 0 and n % m == n // m:
        ans += m

print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    count = 0
    for i in range(1,n):
        for j in range(1,n):
            if (n - j) % i == 0:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += (N-1) // i
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0
    for i in range(1,n):
        for j in range(1,n):
            if i*j >= n:
                break
            if (n-i*j)%j == 0:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    ans = 0
    for i in range(1,n):
        for j in range(1,n):
            if i * j + 1 > n:
                break
            elif i * j + 1 == n:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    result = 0
    for i in range(1, N):
        for j in range(1, N):
            if N - j * i <= 0:
                break
            result += 1
    print(result)
