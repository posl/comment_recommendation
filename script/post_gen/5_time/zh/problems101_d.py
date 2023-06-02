Synthesizing 10/10 solutions

=======
Suggestion 1

def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

=======
Suggestion 2

def main():
    k = int(input())
    count = 0
    i = 1
    while True:
        if i % sum([int(j) for j in str(i)]) == 0:
            count += 1
            if count == k:
                print(i)
                break
        i += 1

=======
Suggestion 3

def S(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 4

def S(n):
    return sum([int(x) for x in str(n)])

=======
Suggestion 5

def S(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
K=int(input())
n=1
while K>0:
    if n%S(n)==0:
        print(n)
        K-=1
    n+=1

=======
Suggestion 6

def s(n):
    return sum(int(i) for i in str(n))

=======
Suggestion 7

def S(n):
    sum = 0
    while n / 10 != 0:
        sum += n % 10
        n = n // 10
    sum += n
    return sum

=======
Suggestion 8

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

K = int(input())
i = 1
while K > 0:
    if S(i) == 1:
        print(i)
        K -= 1
    i += 1

=======
Suggestion 9

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

K = int(input())
n = 0
i = 0
while i < K:
    n += 1
    if n % sum_digits(n) == 0:
        i += 1
        print(n)

=======
Suggestion 10

def S(n):
    return sum(map(int, str(n)))

K = int(input())
N = 0
ans = []
while len(ans) < K:
    N += 1
    if N % S(N) == 0:
        ans.append(N)
for i in ans:
    print(i)
