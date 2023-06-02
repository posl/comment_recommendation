Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    for i in range(2, n):
        if n % i == 0:
            print(i + int(n / i) - 2)
            return

=======
Suggestion 2

def main():
    print("hello world")
    return 0

=======
Suggestion 3

def solve(n):
    # 1. 如果n=2^k，答案是k
    # 2. 否则，答案是k+1，其中k是n的二进制表示中的1的数量
    k = 0
    while n > 0:
        k += n % 2
        n //= 2
    return k

=======
Suggestion 4

def f(n):
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1

n = int(input())
count = 0
while n > 1:
    n = n // f(n)
    count += 1
print(count)

=======
Suggestion 5

def main():
    n = int(input())
    a = int(n ** 0.5)
    while n % a != 0:
        a -= 1
    print(a + n // a - 2)

=======
Suggestion 6

def solve():
    N = int(input())
    count = 0
    while N != 1:
        if N % 2 == 0:
            N /= 2
        else:
            N -= 1
        count += 1
    print(count)

=======
Suggestion 7

def solve(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        tmp = int(n ** 0.5)
        if tmp ** 2 == n:
            return 2 * tmp - 2
        elif n - tmp ** 2 <= tmp:
            return 2 * tmp - 1
        else:
            return 2 * tmp

n = int(input())
print(solve(n))

=======
Suggestion 8

def solve(n):
    #i*j=n
    #i+j最小
    #i=1~n
    #j=n/i
    #j最小
    import math
    j = math.ceil(math.sqrt(n))
    while j > 0:
        if n % j == 0:
            i = n // j
            return i + j - 2
        j -= 1

=======
Suggestion 9

def main():
    n = int(input())
    a = 1
    b = 1
    count = 0
    while a * b < n:
        if a < b:
            a += 1
        else:
            b += 1
        count += 1
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        if i * i > n:
            break
        if n % i == 0:
            ans = i
    print(ans + n // ans - 2)
