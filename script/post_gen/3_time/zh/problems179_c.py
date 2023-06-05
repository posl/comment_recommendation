Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    count = 0
    for i in range(1, n):
        for j in range(1, n):
            if n - i * j > 0:
                count += 1
            else:
                break
    print(count)

=======
Suggestion 2

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
for i in range(1, n):
    divisors = get_divisors(n-i)
    for j in divisors:
        if i <= j:
            ans += 1
print(ans)

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def solve(N):
    result = 0
    for i in range(1, N+1):
        if i * i > N:
            break
        if N % i == 0:
            if i * i == N:
                result += i
            else:
                result += i + N // i
    return result

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        ans += (n - 1) // i
    print(ans)

=======
Suggestion 6

def find(n):
    result = 0
    for c in range(1,n):
        if n % c == 0:
            for b in range(c,n):
                if n % b == 0:
                    a = n / b / c
                    if a >= b:
                        break
                    result += 1
    return result

=======
Suggestion 7

def solve(N):
    ans = 0
    for i in range(1, N):
        ans += (N-1)//i
    return ans

=======
Suggestion 8

def get_divisor(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor

=======
Suggestion 9

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

n = int(input())
ans = 0
for i in range(1, n):
    ans += len(get_divisors(n - i)) - 1
print(ans)
