Synthesizing 10/10 solutions

=======
Suggestion 1

def problem179_c():
    pass

=======
Suggestion 2

def problem179_c():
    n=int(input())
    cnt=0
    for i in range(1,n):
        for j in range(i,n):
            if i*j>=n:
                break
            if n%(i*j)==0:
                cnt+=1
    return cnt

=======
Suggestion 3

def problem179_c(n):
    count = 0
    for i in range(1,n):
        if n % i == 0:
            count += 1
    return count

=======
Suggestion 4

def get_divisors(n):
    """nの約数を全て求める"""
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

n = int(input())
divisors = get_divisors(n)
ans = 0
for i in divisors:
    if i == 1:
        continue
    if (n - i) % i == 0:
        ans += (n - i) // i
print(ans)

=======
Suggestion 5

def get_divisor(n):
    divisor = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)
    return divisor

=======
Suggestion 6

def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

N = int(input())
divisors = get_divisors(N)
count = 0
for i in range(len(divisors)):
    for j in range(i, len(divisors)):
        if N % divisors[i] == 0 and N // divisors[i] % divisors[j] == 0:
            count += 1
print(count)

=======
Suggestion 7

def main():
    n = int(input())
    count = 0
    for c in range(1, n):
        for a in range(1, n):
            if n >= a * c:
                b = n - a * c
                if b <= a:
                    count += 1
                else:
                    break
            else:
                break
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        for j in range(1, N):
            if i*j > N:
                break
            if (N-i*j)%j == 0:
                count += 1
    print(count)

=======
Suggestion 9

def solve(n):
    count = 0
    for i in range(1, n):
        if i * i > n:
            break
        if n % i == 0:
            count += 1
            if i * i < n:
                count += 1
    return count

=======
Suggestion 10

def problem179_c():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            m = N//i - 1
            if m > i:
                ans += m
    print(ans)
