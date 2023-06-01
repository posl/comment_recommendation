Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n):
    if n < 2:
        return 0
    ans = n
    for i in range(2, int(n ** 0.5) + 1):
        if i ** 2 > n:
            break
        j = 2
        while i ** j <= n:
            ans -= 1
            j += 1
    return ans

=======
Suggestion 2

def main():
    n = int(input())
    a = 2
    b = 2
    s = set()
    while a**b <= n:
        while a**b <= n:
            s.add(a**b)
            b += 1
        a += 1
        b = 2
    print(n-len(s))

=======
Suggestion 3

def main():
    N = int(input())
    ans = N
    for b in range(2, int(N**0.5)+1):
        for a in range(2, int(N**0.5)+1):
            if a**b <= N:
                ans -= 1
            else:
                break
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        if i ** 2 > N:
            break
        n = N
        while n % i == 0:
            n //= i
        if n % i == 1:
            ans -= 1
        while n % i == 0:
            n //= i
        if n == 1:
            ans -= 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = N
    for i in range(2,int(N**0.5)+1):
        j = 2
        while i**j <= N:
            ans -= 1
            j += 1
    print(int(ans))

=======
Suggestion 6

def prime_factorization(n):
    if n < 2:
        return []
    elif n == 2:
        return [2]
    elif n == 3:
        return [3]
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return [i] + prime_factorization(n // i)
        return [n]

=======
Suggestion 7

def main():
    N = int(input())
    # 1
    # 1 1
    # 2
    # 2 1
    # 3
    # 3 1
    # 4
    # 2 2
    # 5
    # 5 1
    # 6
    # 6 1
    # 7
    # 7 1
    # 8
    # 2 3
    # 9
    # 3 3
    # 10
    # 10 1
    # 11
    # 11 1
    # 12
    # 12 1
    # 13
    # 13 1
    # 14
    # 14 1
    # 15
    # 15 1
    # 16
    # 2 4
    # 17
    # 17 1
    # 18
    # 18 1
    # 19
    # 19 1
    # 20
    # 20 1
    # 21
    # 21 1
    # 22
    # 22 1
    # 23
    # 23 1
    # 24
    # 24 1
    # 25
    # 5 2
    # 26
    # 26 1
    # 27
    # 3 3
    # 28
    # 28 1
    # 29
    # 29 1
    # 30
    # 30 1
    # 31
    # 31 1
    # 32
    # 2 5
    # 33
    # 33 1
    # 34
    # 34 1
    # 35
    # 35 1
    # 36
    # 6 2
    # 37
    # 37 1
    # 38
    # 38 1
    # 39
    # 39 1
    # 40
    # 40 1
    # 41
    # 41 1

=======
Suggestion 8

def solve():
    n = int(input())
    ans = n
    i = 2
    while i * i <= n:
        j = 2
        while i ** j <= n:
            ans -= 1
            j += 1
        i += 1
    print(ans)

solve()

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    for i in range(2, int(N**0.5) + 1):
        x = i * i
        while x <= N:
            A.append(x)
            x *= i
    print(N - len(set(A)))

main()

=======
Suggestion 10

def main():
    n = int(input())
    ans = n
    for i in range(2, int(n**0.5)+1):
        x = i*i
        while x <= n:
            ans -= 1
            x *= i
    print(ans)
    return 0
