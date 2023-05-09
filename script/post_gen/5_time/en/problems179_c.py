Synthesizing 10/10 solutions

=======
Suggestion 1

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

N = int(raw_input())
f = sorted(list(factors(N)))
count = 0
for i in f:
    for j in f:
        if N%i == 0 and N%(i*j) == 0:
            count += 1
print count

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        ans += (n - 1) // i
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        for j in range(1, N):
            if N - i * j > 0:
                count += 1
            else:
                break
    print(count)

=======
Suggestion 4

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
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            j = N // i
            if i == j:
                ans += 1
            else:
                ans += 2
    print(ans-1)

=======
Suggestion 6

def solve():
    N = int(input())
    count = 0
    for i in range(1, N):
        for j in range(1, N):
            if i * j < N:
                count += 1
            else:
                break
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    count = 0
    for i in range(1, n):
        for j in range(1, n):
            if i * j + 1 > n:
                break
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    answer = 0
    for i in range(1, n):
        for j in range(1, n):
            if i*j < n:
                answer += 1
            else:
                break
    print(answer)

=======
Suggestion 9

def main():
    n = int(input())
    result = 0
    for i in range(1,n):
        result += (n-1)//i
    print(result)

=======
Suggestion 10

def get_input():
    return int(input())
