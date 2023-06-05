Synthesizing 10/10 solutions

=======
Suggestion 1

def S(n):
    sum = 0
    while n>0:
        sum += n%10
        n = n//10
    return sum

K = int(input())
n = 1
while K>0:
    if S(n) == 1:
        print(n)
        K -= 1
    n += 1

=======
Suggestion 2

def snuke(n):
    return n/sum([int(x) for x in str(n)])

=======
Suggestion 3

def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

=======
Suggestion 4

def S(n):
    # 计算n的十进制数字之和
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum

=======
Suggestion 5

def S(n):
    sum = 0
    while n > 0:
        sum += n%10
        n = n//10
    return sum

=======
Suggestion 6

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 7

def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 8

def s(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 9

def S(n):
    sum = 0
    while n:
        sum += n%10
        n = n/10
    return sum

=======
Suggestion 10

def snuke(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

k = int(input())
n = 1
while k > 0:
    if snuke(n) == 1:
        print(n)
        k -= 1
    n += 1
