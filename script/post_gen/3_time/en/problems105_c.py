Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N == 0:
        print(0)
    else:
        ans = ""
        while N != 0:
            if N % 2 == 0:
                ans += "0"
            else:
                ans += "1"
                N -= 1
            N //= -2
        print(ans[::-1])

=======
Suggestion 2

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ""
    while N != 0:
        if N % 2 == 0:
            ans += "0"
            N //= -2
        else:
            ans += "1"
            N = (N - 1) // -2
    print(ans[::-1])

=======
Suggestion 3

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ""
    while N != 0:
        if N % 2 == 0:
            ans = "0" + ans
            N = N // -2
        else:
            ans = "1" + ans
            N = (N - 1) // -2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    S = []
    while N != 0:
        if N % 2 == 0:
            S.append(0)
            N //= -2
        else:
            S.append(1)
            N = (N - 1) // -2
    print("".join(map(str, reversed(S))))

=======
Suggestion 5

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ''
    while N != 0:
        if N % 2 == 0:
            ans = '0' + ans
            N = N // -2
        else:
            ans = '1' + ans
            N = (N - 1) // -2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    if N == 0:
        print(0)
    else:
        S = ''
        while N != 0:
            if N % 2 == 0:
                S = '0' + S
                N //= -2
            else:
                S = '1' + S
                N = (N - 1) // -2
        print(S)

=======
Suggestion 7

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = []
    while N != 0:
        if N % 2 == 0:
            ans.append('0')
            N = N // (-2)
        else:
            ans.append('1')
            N = (N - 1) // (-2)
    print(''.join(ans[::-1]))

=======
Suggestion 8

def main():
    n = int(input())
    if n == 0:
        print(0)
    else:
        s = ''
        while n:
            if n % (-2) == 0:
                s = '0' + s
                n //= (-2)
            else:
                s = '1' + s
                n = (n - 1) // (-2)
        print(s)

=======
Suggestion 9

def base_minus2(n):
    if n == 0:
        return '0'
    s = ''
    while n:
        s += str(n % -2)
        n = (n - n % -2) // -2
    return s[::-1]

=======
Suggestion 10

def base_m(N, m):
    if N == 0:
        return '0'
    elif N < 0:
        N = -N
        minus = True
    else:
        minus = False
    ans = ''
    while N > 0:
        ans = str(N % m) + ans
        N //= m
    if minus:
        ans = '-' + ans
    return ans
