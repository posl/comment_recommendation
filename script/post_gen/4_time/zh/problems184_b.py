Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N,X = map(int,input().split())
    S = input()

    for i in range(N):
        if S[i] == 'o':
            X += 1
        else:
            if X > 0:
                X -= 1

    print(X)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'o':
            ans += 1
        else:
            ans = max(0, ans - 1)
    print(ans)

=======
Suggestion 3

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
Suggestion 4

def solve():
    N, X = map(int, input().split())
    S = input()
    score = X
    for s in S:
        if s == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    print(score)

=======
Suggestion 5

def main():
    n,x = map(int,input().split())
    s = input()
    score = x
    for i in range(n):
        if s[i] == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    print(score)

=======
Suggestion 6

def get_input():
    n, x = map(int, input().split())
    s = input()
    return n, x, s

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    S = input()
    result = X
    for i in range(N):
        if S[i] == 'o':
            result += 1
        else:
            if result > 0:
                result -= 1
    print(result)

=======
Suggestion 8

def main():
    N,X = [int(x) for x in input().split()]
    S = input()
    score = X
    for c in S:
        if c == 'o':
            score += 1
        elif c == 'x' and score > 0:
            score -= 1
    print(score)

=======
Suggestion 9

def solve():
    n,x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'o':
            ans += 1
        elif ans > 0:
            ans -= 1
    print(ans)
