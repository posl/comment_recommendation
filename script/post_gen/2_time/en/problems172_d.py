Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += i * (N // i) * ((N // i) + 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += i * (n // i) * (n // i + 1) // 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    divisors = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            divisors[j] += 1
    ans = 0
    for i in range(1, N+1):
        ans += i * divisors[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * (N // i) * (N // i + 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * (N//i) * (N//i + 1) // 2
    print(ans)

main()

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += (i * (N//i) * (N//i+1))//2
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += (N//i) * i
    print(ans)

=======
Suggestion 8

def f(n):
    r = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            r += i
            if n // i != i:
                r += n // i
    return r

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        #print(i, N//i, (N//i)*(N//i+1)//2, i*((N//i)*(N//i+1)//2))
        ans += i*((N//i)*(N//i+1)//2)
    print(ans)
