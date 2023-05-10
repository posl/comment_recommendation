Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N = int(input())
    ans = 0
    for i in range(1, 10**6):
        if (N - i*(i+1)//2) % i == 0 and (N - i*(i+1)//2) // i >= 0:
            ans += 1
    print(ans*2)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, 10**6):
        if (2*n-i*i+i)%(2*i) == 0:
            ans += 1
    print(ans*2)

=======
Suggestion 3

def main():
    N = int(input())
    cnt = 0
    for i in range(1,N):
        if N % i == 0:
            if (N // i) % 2 == 1:
                cnt += 1
    print(cnt*2)
main()

=======
Suggestion 4

def solve():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if N % i == 0:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i * (i + 1) // 2 >= n:
            ans = i
            break
    print(ans)

=======
Suggestion 6

def solve(n):
    cnt = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i % 2 == 1:
                cnt += 2
            if i**2 == n:
                cnt -= 1
    return cnt
n = int(input())
print(solve(n))

=======
Suggestion 7

def main():
    n = int(input())
    import math
    count = 0
    for i in range(1, int(math.sqrt(n*2)) + 1):
        if (n * 2) % i == 0:
            if (n * 2 // i - i + 1) % 2 == 0:
                count += 1
    print(count * 2)

=======
Suggestion 8

def solve(n):
    i = 1
    ans = 0
    while i * (i + 1) <= 2 * n:
        if (2 * n + i - i * i) % (2 * i) == 0:
            ans += 1
        i += 1
    return ans * 2

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if (i*(i+1))//2 == N:
            ans += 1
        elif (i*(i+1))//2 > N:
            break
    print(ans*2)
