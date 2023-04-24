Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
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

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
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
Suggestion 3

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
Suggestion 4

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'o':
            x += 1
        elif s[i] == 'x':
            if x > 0:
                x -= 1
            else:
                pass
    print(x)

=======
Suggestion 5

def problems184_b():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'o':
            ans += 1
        elif s[i] == 'x':
            if ans > 0:
                ans -= 1
    print(ans)

=======
Suggestion 6

def main():
    N,X = map(int,input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'o':
            ans += 1
        else:
            if ans > 0:
                ans -= 1
    print(ans)

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    s = input()
    score = x
    for i in s:
        if i == 'o':
            score += 1
        else:
            if score == 0:
                continue
            else:
                score -= 1
    print(score)

=======
Suggestion 8

def calc_score(s, x):
    score = x
    for i in range(len(s)):
        if s[i] == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    return score
