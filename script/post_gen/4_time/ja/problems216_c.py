Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = ''
    while n > 0:
        if n % 2 == 0:
            n //= 2
            ans = 'B' + ans
        else:
            n -= 1
            ans = 'A' + ans
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = []
    while N > 0:
        if N % 2 == 0:
            N //= 2
            ans.append('B')
        else:
            N -= 1
            ans.append('A')
    print(''.join(ans[::-1]))

=======
Suggestion 3

def main():
    n = int(input())
    s = ""
    while n > 0:
        if n % 2 == 0:
            s += "B"
            n //= 2
        else:
            s += "A"
            n -= 1
    print(s[::-1])

=======
Suggestion 4

def main():
    n = int(input())
    s = ""
    while n > 0:
        if n % 2 == 0:
            s = "B" + s
            n //= 2
        else:
            s = "A" + s
            n -= 1
    print(s)

=======
Suggestion 5

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            S = "B" + S
            N = N // 2
        else:
            S = "A" + S
            N -= 1
    print(S)

=======
Suggestion 6

def main():
    N = int(input())
    ans = []
    while N > 0:
        if N % 2 == 0:
            N = N // 2
            ans.append('B')
        else:
            N -= 1
            ans.append('A')
    ans.reverse()
    print(''.join(ans))

=======
Suggestion 7

def main():
    N = int(input())
    ans = []
    while N > 0:
        if N % 2 == 0:
            N = N // 2
            ans.append('B')
        else:
            N -= 1
            ans.append('A')
    print(''.join(ans[::-1]))

=======
Suggestion 8

def solve():
    N = int(input())
    ans = ""
    while N > 0:
        if N % 2 == 0:
            N = N // 2
            ans = "B" + ans
        else:
            N -= 1
            ans = "A" + ans
    print(ans)
    return 0

=======
Suggestion 9

def solve():
    n = int(input())
    ans = ""
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            ans = "B" + ans
        else:
            n = n - 1
            ans = "A" + ans
    print(ans)

=======
Suggestion 10

def solve():
    n=int(input())
    res=[]
    while n>0:
        if n%2==0:
            n//=2
            res.append('B')
        else:
            n-=1
            res.append('A')
    print(''.join(reversed(res)))
solve()
