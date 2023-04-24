Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    if n == 0:
        print(0)
        exit()
    ans = ''
    while n != 0:
        if n % (-2) == 0:
            ans = '0' + ans
        else:
            ans = '1' + ans
            n -= 1
        n //= (-2)
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ""
    while N != 0:
        if N % 2 == 0:
            ans = "0" + ans
            N //= -2
        else:
            ans = "1" + ans
            N = (N - 1) // -2
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ""
    while N != 0:
        if N % (-2) == 0:
            ans += "0"
        else:
            ans += "1"
            N -= 1
        N //= (-2)
    print(ans[::-1])

=======
Suggestion 4

def main():
    n = int(input())
    s = ''
    while n != 0:
        r = n % (-2)
        n = n // (-2)
        if r < 0:
            r += 2
            n += 1
        s = str(r) + s
    if s == '':
        s = '0'
    print(s)

=======
Suggestion 5

def calc(n):
    if n == 0:
        return '0'
    ans = ''
    while n != 0:
        if n % 2 == 0:
            ans = '0' + ans
        else:
            ans = '1' + ans
            n -= 1
        n //= -2
    return ans

n = int(input())
print(calc(n))

=======
Suggestion 6

def toMinus2(num):
    if num == 0:
        return '0'
    s = ''
    while num != 0:
        if num % 2 == 0:
            s = '0' + s
        else:
            s = '1' + s
            num -= 1
        num //= -2
    return s

N = int(input())
print(toMinus2(N))

=======
Suggestion 7

def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())

    if n == 0:
        print(0)
        return
    ans = []
    while n != 0:
        if n % 2 == 0:
            ans.append(0)
            n //= -2
        else:
            ans.append(1)
            n = (n-1) // -2
    ans.reverse()
    print(''.join(map(str, ans)))

=======
Suggestion 8

def main():
    N = int(input())
    ans = ""
    if N == 0:
        ans = "0"
    while N != 0:
        ans += str(abs(N%(-2)))
        N -= abs(N%(-2))
        N //= (-2)
    print(ans[::-1])

=======
Suggestion 9

def n2(num, base):
    if num == 0:
        return "0"
    ans = ""
    while num != 0:
        num, mod = divmod(num, base)
        if mod < 0:
            num, mod = num + 1, mod + abs(base)
        ans = str(mod) + ans
    return ans

num = int(input())
print(n2(num, -2))

=======
Suggestion 10

def to_n_ary(n, ary):
    if n == 0:
        return ary
    if n % (-2) == 0:
        ary.append("0")
        return to_n_ary(n // (-2), ary)
    else:
        ary.append("1")
        return to_n_ary((n - 1) // (-2), ary)

n = int(input())
