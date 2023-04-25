Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += i * (N // i) * (N // i + 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * (N//i) * ((N//i)+1) // 2
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * (N//i) * (N//i+1) // 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * (N//i)
    print(ans)

main()

=======
Suggestion 5

def divisorCount(n):
    if n == 1:
        return 1
    count = 2
    i = 2
    while i*i < n:
        if n % i == 0:
            count += 2
        i += 1
    if i*i == n:
        count += 1
    return count

=======
Suggestion 6

def f(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        return 2*f(x//2)
    else:
        return 2*f((x+1)//2)

N = int(input())
ans = 0
for i in range(1, N+1):
    ans += i*f(i)
print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    print(sum(K*divisors(K) for K in range(1, N+1)))

=======
Suggestion 8

def solve(n):
