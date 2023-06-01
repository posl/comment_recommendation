Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    count = 0
    for i in range(1,n):
        for j in range(i,n):
            if i*j < n:
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

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        ans += (n - 1) // i
    print(ans)

=======
Suggestion 4

def problem179_c(n):
    cnt = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j < n:
                cnt += 1
            else:
                break
    return cnt

=======
Suggestion 5

def solve(n):
    count = 0
    for c in range(1, n):
        if n % c == 0:
            count += n // c - 1
        else:
            count += n // c
    return count

=======
Suggestion 6

def problem179_c():
    pass

=======
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        for j in range(1, N):
            if i * j > N:
                break
            if (N - i * j) % j == 0:
                count += 1
    print(count)

=======
Suggestion 8

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n//i)
    return divisors

N = int(input())
ans = 0
for i in range(1, N):
    ans += len(get_divisors(N-i))-1
print(ans)
