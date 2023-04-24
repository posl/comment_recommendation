Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = []
    while N != 0:
        if N % 2 == 0:
            ans.append(0)
            N //= -2
        else:
            ans.append(1)
            N = (N - 1) // -2
    print(''.join(map(str, ans[::-1])))

=======
Suggestion 3

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
            n = (n-1) // -2
    print(''.join(str(i) for i in ans[::-1]))

=======
Suggestion 4

def main():
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
Suggestion 5

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    S = ''
    while N != 0:
        if N % 2 == 0:
            S += '0'
            N //= -2
        else:
            S += '1'
            N = (N - 1) // -2
    print(S[::-1])

=======
Suggestion 6

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    s = ""
    while N != 0:
        if N % 2 == 0:
            s += "0"
            N //= -2
        else:
            s += "1"
            N = (N - 1) // -2
    print(s[::-1])

=======
Suggestion 7

def main():
    n = int(input())
    if n == 0:
        print('0')
        return
    ans = ''
    while n != 0:
        if n % 2 == 0:
            ans += '0'
            n //= -2
        else:
            ans += '1'
            n = (n - 1) // -2
    print(ans[::-1])

=======
Suggestion 8

def main():
    N = int(input())
    if N == 0:
        print(0)
    else:
        ans = ""
        while N != 0:
            if N%2 == 0:
                ans += "0"
                N //= 2
            else:
                ans += "1"
                N = (N-1)//2
        print(ans[::-1])

=======
Suggestion 9

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    res = ""
    while N != 0:
        if N % 2 == 0:
            res += "0"
            N //= -2
        else:
            res += "1"
            N = (N - 1) // -2
    print(res[::-1])

=======
Suggestion 10

def main():
    N = int(input())
    S = []
    while N != 0:
        S.append(str(N % 2))
        N = -(N // 2)
    if len(S) == 0:
        print("0")
    else:
        print("".join(S))

main()
