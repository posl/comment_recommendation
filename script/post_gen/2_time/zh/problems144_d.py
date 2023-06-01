Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            ans = i
            break
    if ans == 0:
        ans = N
    print(ans - 1)

=======
Suggestion 2

def solve(n):
    a = 1
    b = n
    while a < b:
        mid = int((a + b) / 2)
        if mid * mid < n:
            a = mid + 1
        else:
            b = mid
    return a + n - a * a

=======
Suggestion 3

def solve():
    N = int(input())
    if N == 2:
        print(1)
        return
    if N == 3:
        print(2)
        return
    if N == 4:
        print(3)
        return
    if N == 5:
        print(3)
        return
    if N == 6:
        print(4)
        return
    if N == 7:
        print(4)
        return
    if N == 8:
        print(4)
        return
    if N == 9:
        print(4)
        return
    if N == 10:
        print(5)
        return
    if N == 11:
        print(5)
        return
    if N == 12:
        print(5)
        return
    if N == 13:
        print(5)
        return
    if N == 14:
        print(5)
        return
    if N == 15:
        print(5)
        return
    if N == 16:
        print(5)
        return
    if N == 17:
        print(5)
        return
    if N == 18:
        print(5)
        return
    if N == 19:
        print(5)
        return
    if N == 20:
        print(5)
        return
    if N == 21:
        print(5)
        return
    if N == 22:
        print(6)
        return
    if N == 23:
        print(6)
        return
    if N == 24:
        print(6)
        return
    if N == 25:
        print(6)
        return
    if N == 26:
        print(6)
        return
    if N == 27:
        print(6)
        return
    if N == 28:
        print(6)
        return
    if N == 29:
        print(6)
        return
    if N == 30:
        print(6)
        return
    if N == 31:
        print(6)
        return
    if N == 32:
        print(6)
        return
    if N == 33:
        print(6)
        return
    if N == 34:
        print(6)

=======
Suggestion 4

def solve(n):
    ans = 1
    while ans * ans < n:
        ans += 1
    if ans * ans == n:
        return 2 * ans - 2
    elif (ans - 1) * ans < n <= (ans - 1) * ans + ans:
        return 2 * ans - 1
    else:
        return 2 * ans

n = int(input())
print(solve(n))

=======
Suggestion 5

def main():
    n = int(input())
    count = 0
    while n != 2:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        count += 1
    print(count + 2)

=======
Suggestion 6

def main():
    N = int(input())
    i = 1
    j = 1
    while i * j < N:
        if i < j:
            i += 1
        else:
            j += 1
    print(i+j-2)

=======
Suggestion 7

def solve():
    n = int(input())
    ans = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans = i + n//i - 2
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    x = 1
    y = 1
    while x*y < n:
        if x < y:
            x += 1
        else:
            y += 1
    print(x+y-2)

=======
Suggestion 9

def solve():
    n = int(input())
    ans = 0
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
            ans += 1
    if n > 1:
        ans += 1
    print(ans)

solve()

=======
Suggestion 10

def main():
    pass
