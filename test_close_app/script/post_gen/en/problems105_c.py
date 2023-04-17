Synthesizing 10/10 solutions (Duplicates hidden)

=======

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
            N = N // -2 + 1
    print(ans[::-1])

=======

def main():
    N = int(input())
    if N == 0:
        print(0)
    else:
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

def main():
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
    print(''.join(map(str, ans[::-1])))

=======

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = []
    while n != 0:
        if n % 2 == 0:
            ans.append(0)
            n = n // (-2)
        else:
            ans.append(1)
            n = (n - 1) // (-2)
    print(*ans[::-1], sep='')

=======

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = []
    while n != 0:
        if n % 2 == 0:
            ans.append(0)
            n = n // (-2)
        else:
            ans.append(1)
            n = (n - 1) // (-2)
    print(''.join(map(str, ans[::-1])))

=======

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    S = ''
    while N != 0:
        if N % 2 == 0:
            S = '0' + S
            N = N // 2
        else:
            S = '1' + S
            N = (N - 1) // 2
    print(S)

=======

def main():
    n = int(input())
    if n == 0:
        print(0)
        return

    s = ""
    while n != 0:
        if n % 2 == 0:
            s += "0"
            n //= -2
        else:
            s += "1"
            n = (n - 1) // -2
    print(s[::-1])

=======

def main():
    N = int(input())
    if N == 0:
        print(0)
    else:
        ans = ""
        while N != 0:
            if N%2 == 0:
                ans = "0" + ans
            else:
                ans = "1" + ans
                N -= 1
            N //= -2
        print(ans)

=======

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = []
    while N:
        if N % 2:
            ans.append(1)
            N -= 1
        else:
            ans.append(0)
        N //= -2
    print(''.join(map(str, ans[::-1])))
