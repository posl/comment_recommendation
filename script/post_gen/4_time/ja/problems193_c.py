Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = N
    i = 2
    while i*i <= N:
        j = 2
        while i**j <= N:
            ans -= 1
            j += 1
        i += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = n
    for i in range(2, int(n**0.5)+1):
        j = 2
        while i**j <= n:
            ans -= 1
            j += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = N
    for i in range(2, int(N**0.5)+1):
        j = 2
        while i**j <= N:
            ans -= 1
            j += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = N
    for i in range(2, int(N**0.5)+1):
        for j in range(2, int(N**0.5)+1):
            if i**j <= N:
                ans -= 1
            else:
                break
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        tmp = i ** 2
        while tmp <= N:
            ans -= 1
            tmp *= i
    print(ans)

=======
Suggestion 6

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

    print(n - len(s))

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    for i in range(2, int(n ** 0.5) + 1):
        power = i ** 2
        while power <= n:
            ans += 1
            power *= i
    print(n - ans)

=======
Suggestion 8

def main():
    N = int(input())
    if N == 1:
        print(0)
        exit()
    ans = N
    for i in range(2, int(N**0.5)+1):
        tmp = i
        while tmp <= N:
            tmp *= i
            ans -= 1
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    ans = N
    # 2^60 > 10^10
    for i in range(2, 60):
        for j in range(2, 60):
            if i ** j <= N:
                ans -= 1
            else:
                break
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    ans = N - 1

    # 2^b で表せる数を引いていく
    b = 2
    while b * b <= N:
        # 2^b で表せる数
        x = b * b
        while x <= N:
            ans -= 1
            x *= b
        b += 1

    print(ans)
