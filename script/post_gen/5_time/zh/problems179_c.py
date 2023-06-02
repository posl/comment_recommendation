Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        for j in range(i, N):
            if i * j < N:
                count += 1
            else:
                break
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(1,N):
        for j in range(1,N):
            if i*j < N:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    count = 0
    for i in range(1,N):
        if N % i == 0:
            if i == N/i:
                count += 1
            else:
                count += 2
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    count = 0
    for i in range(1,int(N**0.5)+1):
        if N%i == 0:
            if N//i != i:
                count += (N//i-1)
            else:
                count += (N//i-1)
    print(count)

=======
Suggestion 5

def f(n):
    ans = 0
    for i in range(1, n):
        ans += (n-1) // i
    return ans

n = int(input())
print(f(n))

=======
Suggestion 6

def main():
    n = int(input().strip())
    ans = 0
    for i in range(1, n):
        ans += (n - 1) // i
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        ans += (n - 1) // i
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j < n:
                cnt += 1
            else:
                break
    print(cnt)

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    for i in range(1,N):
        ans += (N-1)//i
    print(ans)
