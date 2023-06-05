Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n):
    res = 0
    for i in range(1, n):
        res += (n - 1) // i
    return res

=======
Suggestion 2

def main():
    n = int(input())
    count = 0
    for a in range(1, n):
        for b in range(1, n):
            if a*b < n:
                count += 1
            else:
                break
    print(count)

=======
Suggestion 3

def problem179_c():
    N = int(input())
    count = 0
    for i in range(1, N):
        if N % i == 0:
            count += 1
    print(count)
problem179_c()

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1,N):
        ans += (N-1)//i
    print(ans)
main()

=======
Suggestion 5

def solve(n):
    count = 0
    for i in range(1,n):
        if n%i == 0:
            count += 1
    return count

=======
Suggestion 6

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def solve(n):
    cnt = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j < n:
                cnt += 1
            else:
                break
    return cnt

=======
Suggestion 9

def solve(n):
    count = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j >= n:
                break
            else:
                count += 1
    return count
