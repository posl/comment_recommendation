Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = ''
    while n != 0:
        if n % 2 == 0:
            ans = '0' + ans
        else:
            ans = '1' + ans
            n -= 1
        n //= -2
    if ans == '':
        ans = '0'
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = ""
    while n != 0:
        if n % 2 == 0:
            ans += "0"
        else:
            ans += "1"
            n -= 1
        n //= -2
    print(ans[::-1])

=======
Suggestion 3

def main():
    n = int(input())
    if n == 0:
        print(0)
        exit()
    ans = ''
    while n != 0:
        if n % 2 == 0:
            ans = '0' + ans
            n //= -2
        else:
            ans = '1' + ans
            n = (n - 1) // -2
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    if n == 0:
        print(0)
        exit()
    ans = ''
    while n != 0:
        if n % 2 == 0:
            ans += '0'
        else:
            ans += '1'
            n -= 1
        n //= -2
    print(ans[::-1])

=======
Suggestion 5

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    s = ""
    while n != 0:
        if n % 2 == 0:
            s = "0" + s
        else:
            s = "1" + s
            n -= 1
        n //= -2
    print(s)

=======
Suggestion 6

def solve():
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
            n = (n - 1) // -2
    ans.reverse()
    print(''.join(map(str, ans)))

=======
Suggestion 7

def main():
    n = int(input())
    if n == 0:
        print(0)
        exit()
    ans = ""
    while n != 0:
        if n % 2 != 0:
            ans = "1" + ans
            n -= 1
        else:
            ans = "0" + ans
        n //= -2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())

    if N == 0:
        print(0)
        return

    ans = ''
    while N != 0:
        if N % (-2) != 0:
            ans = '1' + ans
            N -= 1
        else:
            ans = '0' + ans
        N //= (-2)

    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ""
    while N != 0:
        ans = str(N & 1) + ans
        N = -(N >> 1)
    print(ans)

=======
Suggestion 10

def calc_binary(n):
    if n == 0:
        return "0"
    ans = ""
    while n != 0:
        if n % 2 == 0:
            ans = "0" + ans
        else:
            ans = "1" + ans
            n -= 1
        n //= -2
    return ans
