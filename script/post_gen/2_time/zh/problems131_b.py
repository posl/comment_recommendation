Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, l = map(int, input().split())
    if l >= 0:
        ans = sum(list(range(l+1, l+n)))
    elif l+n-1 <= 0:
        ans = sum(list(range(l, l+n)))
    else:
        ans = sum(list(range(l, l+n-1))) + l+n-1
    print(ans)

=======
Suggestion 2

def main():
    n, l = map(int, input().split())
    if l >= 0:
        print(sum(range(l+1, l+n)))
    else:
        if n <= -l:
            print(sum(range(l+n, l)))
        else:
            print(sum(range(l+1, l+n)))

=======
Suggestion 3

def solve():
    n, l = map(int, input().split())
    ans = 0
    if l >= 0:
        ans = (l + n - 1) * (l + n) // 2 - l * (l - 1) // 2
    else:
        if l + n - 1 >= 0:
            ans = (l + n - 1) * (l + n) // 2
        else:
            if l + n >= 0:
                ans = (l + n) * (l + n + 1) // 2 - l * (l + 1) // 2
            else:
                ans = (l + n) * (l + n + 1) // 2 - (l + n - 1) * (l + n) // 2
    print(ans)

=======
Suggestion 4

def main():
    n, l = map(int, input().split())
    print(sum(range(l+1, l+n)))

=======
Suggestion 5

def main():
    N, L = map(int, input().split())
    sum = 0
    for i in range(N):
        sum += L+i
    if L >= 0:
        sum -= L
    elif L+N-1 < 0:
        sum -= L+N-1
    print(sum)

=======
Suggestion 6

def main():
    n,l = map(int,raw_input().split())
    print sum(range(l+1,l+n)) - (l+1)

=======
Suggestion 7

def main():
    n, l = map(int, input().split())

    ans = 0
    for i in range(1, n + 1):
        ans += l + i - 1

    if ans > 0:
        ans -= l + n - 1
    elif ans < 0:
        ans -= l

    print(ans)

=======
Suggestion 8

def main():
    n,l = map(int,input().split())
    if l > 0:
        print(sum(range(l+1,l+n)))
    elif l+n <= 0:
        print(sum(range(l+n,l)))
    else:
        print(sum(range(l,l+n)))

=======
Suggestion 9

def main():
    n, l = map(int, input().split())
    if n == 2:
        print(l)
    elif l >= 0:
        print(sum(range(l+1, l+n)))
    elif l+n-1 <= 0:
        print(sum(range(l, l+n-1)))
    else:
        print(sum(range(l, 0)) + sum(range(1, l+n-1)))

=======
Suggestion 10

def main():
    n,l=map(int,input().split())
    min=1000000
    sum=0
    for i in range(n):
        sum+=l+i
        if abs(l+i)<abs(min):
            min=l+i
    print(sum-min)
