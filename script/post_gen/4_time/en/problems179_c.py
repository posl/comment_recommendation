Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        ans += (n - 1) // i
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for a in range(1, n):
        for b in range(1, n):
            if a * b >= n:
                break
            ans += 1
    print(ans)

=======
Suggestion 3

def solve(n):
    ans = 0
    for i in range(1,n+1):
        ans += (n-1)//i
    return ans

n = int(input())
print(solve(n))

=======
Suggestion 4

def main():
    N = int(input())
    cnt = 0
    for i in range(1,int(N**0.5)+1):
        if N%i == 0:
            if i == N//i:
                cnt += i-1
            else:
                cnt += N//i-1
    print(cnt)

=======
Suggestion 5

def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        if N % i == 0:
            count += N // i - 1

    print(count)

=======
Suggestion 6

def solve(n):
    count = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j + i + j > n:
                break
            if (n - i - j) % (i * j) == 0:
                count += 1
    return count

=======
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        if i*i > N:
            break
        if N % i == 0:
            count += 1
            if i*i != N:
                count += 1
    print(count)

=======
Suggestion 8

def count(n):
    ans = 0
    for i in range(1, n):
        ans += (n-1)//i
    return ans

n = int(input())
print(count(n))

=======
Suggestion 9

def main():
    N = int(input())
    #N = 1000000
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j < N:
                cnt += 1
            else:
                break
    print(cnt)

=======
Suggestion 10

def problem179_c():
    N = int(input())
    #print(N)
    count = 0
    for a in range(1, N):
        for b in range(1, N):
            c = N - a * b
            if c > 0:
                count += 1
            else:
                break
    print(count)
