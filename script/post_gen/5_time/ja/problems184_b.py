Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in s:
        if i == 'x':
            ans = max(0, ans - 1)
        else:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    s = input()
    
    for i in range(n):
        if s[i] == 'o':
            x += 1
        else:
            if x > 0:
                x -= 1
    print(x)

=======
Suggestion 3

def main():
    n,x = map(int,input().split())
    s = input()
    result = x
    for i in range(n):
        if s[i] == 'o':
            result += 1
        elif result > 0:
            result -= 1
    print(result)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'o':
            ans += 1
        elif ans > 0:
            ans -= 1
    print(ans)

=======
Suggestion 5

def main():
    n,x = map(int,input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'o':
            ans += 1
        else:
            if ans > 0:
                ans -= 1
    print(ans)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'o':
            X += 1
        else:
            if X > 0:
                X -= 1
    print(X)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    s = input()
    p = x
    for i in range(n):
        if s[i] == 'o':
            p += 1
        else:
            if p > 0:
                p -= 1
    print(p)

=======
Suggestion 8

def solve():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'o':
            ans += 1
        else:
            if ans > 0:
                ans -= 1
    print(ans)
