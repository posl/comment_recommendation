Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if (n - i * (i - 1) // 2) % i == 0:
            ans += 1
    print(ans * 2)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n**0.5)+1):
        if (2*n-i*i+i) % (2*i) == 0:
            ans += 1
    print(ans*2)

=======
Suggestion 3

def solve():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            if (N//i)%2 == 1:
                ans += 2
            if i*i == N:
                ans -= 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    i = 1
    count = 0
    while i * i <= 2 * N:
        if (2 * N) % i == 0:
            if (i + (2 * N) // i - 1) % 2 == 0:
                count += 1
        i += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            if N / i % 2 == 1:
                count += 1
    print(count * 2)

=======
Suggestion 6

def main():
    N = int(input())
    N = N*8 +1
    N = int(N**0.5)
    N = N-1
    N = N//2
    print(N)

=======
Suggestion 7

def solve(n):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    if n == 1:
        return 2
    else:
        sum = 0
        i = 1
        while sum < n:
            sum += i
            i += 1
        if sum == n:
            return i - 1
        else:
            return i - 2

=======
Suggestion 8

def main():
    N = int(input())
    #N = 963761198400
    #N = 1000000000000
    #N = 12
    #N = 1
    i = 1
    n = 0
    while True:
        if N <= i:
            break
        n += 1
        i += n
    print(n)

=======
Suggestion 9

def main():
    N = int(input())
    n = int((N*2)**0.5)
    print(n)
    count = 0
    while n*(n+1)//2 <= N:
        count += 1
        n += 1
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    #print(n)
    #print(n*(n-1)//2)
    #print(n*(n+1)//2)
    for i in range(1, n):
        if i*(i+1)//2 > n:
            break
    i -= 1
    print(i)
