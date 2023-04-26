Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if n % i == 0:
            if i % 2 == 1:
                ans += 1
    print(ans*2)

=======
Suggestion 2

def solve():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if i * (i + 1) // 2 >= N:
            ans = i
            break
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    ans = 0
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            if i%2 == n//i%2:
                ans += 1
    print(ans*2)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i * (i + 1) // 2 > N:
            break
        if (N - i * (i + 1) // 2) % i == 0:
            ans += 1
    print(ans * 2)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N % i == 0 and (N//i-i) % 2 == 1:
            ans += 1
    print(ans*2)

=======
Suggestion 6

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if i*(i+1)/2 > N:
            break
        if (N-i*(i+1)/2)%i == 0:
            count += 1
    print(count*2)

=======
Suggestion 7

def solve():
    N = int(input())
    ans = 0
    for i in range(1, int(N ** 0.5)+1):
        if N % i == 0:
            if i % 2 == 1:
                ans += 2
            if N // i != i and (N // i) % 2 == 1:
                ans += 2
    print(ans)

=======
Suggestion 8

def calc(n):
    ans = 0
    for i in range(1,n+1):
        if i*(i+1)//2 > n:
            break
        if (n-i*(i+1)//2) % i == 0:
            ans += 1
    return ans*2

n = int(input())
print(calc(n))

=======
Suggestion 9

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if n/i - i/2 > 0 and (n/i - i/2) % 1 == 0:
            ans += 1
    print(ans*2)

=======
Suggestion 10

def main():
    n = int(input())
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    print(count)
