Synthesizing 10/10 solutions

=======

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ""
    while N != 0:
        if N % -2 == 0:
            ans += "0"
            N //= -2
        else:
            ans += "1"
            N = (N - 1) // -2
    print(ans[::-1])

=======

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = ''
    while n != 0:
        if n % 2 == 0:
            ans = '0' + ans
            n //= -2
        else:
            ans = '1' + ans
            n = n // -2 + 1
    print(ans)

=======

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ''
    while N != 0:
        if N % 2 == 0:
            ans = '0' + ans
            N //= -2
        else:
            ans = '1' + ans
            N = N // -2 + 1
    print(ans)

=======

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ''
    while N != 0:
        if N % (-2) == 0:
            ans += '0'
            N = N // (-2)
        else:
            ans += '1'
            N = (N - 1) // (-2)
    print(ans[::-1])

=======

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = []
    while N != 0:
        if N % -2 == 0:
            ans.append(0)
            N = N // -2
        else:
            ans.append(1)
            N = (N - 1) // -2
    print(''.join(map(str,ans[::-1])))

=======

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    S = ''
    while N != 0:
        if N % (-2) == 0:
            S = '0' + S
            N = N // (-2)
        else:
            S = '1' + S
            N = N // (-2) + 1
    print(S)

=======

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    a = []
    while N != 0:
        if N % (-2) == 0:
            a.append(0)
            N = N // (-2)
        else:
            a.append(1)
            N = (N - 1) // (-2)
    a = a[::-1]
    print(*a, sep='')

=======

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = ''
    while n != 0:
        ans += str(n % -2)
        n = (n - n % -2) // -2
    print(ans[::-1])

=======

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ''
    while N:
        ans = str(N % -2) + ans
        N = (N - (N % -2)) // -2
    print(ans)

=======

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ''
    while True:
        if N % 2 == 1:
            N -= 1
            ans += '1'
        else:
            ans += '0'
        N //= -2
        if N == 0:
            break
    print(ans[::-1])
