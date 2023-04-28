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
Suggestion 3

def main():
    n, x = map(int, input().split())
    s = input()
    points = x
    for i in range(n):
        if s[i] == 'o':
            points += 1
        else:
            if points > 0:
                points -= 1
    print(points)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    S = input()
    for c in S:
        if c == 'o':
            X += 1
        else:
            if X > 0:
                X -= 1
    print(X)

=======
Suggestion 5

def main():
    n,x = map(int,input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == "o":
            ans += 1
        else:
            if ans > 0:
                ans -= 1
    print(ans)

=======
Suggestion 6

def main():
    N,X = map(int,input().split())
    S = input()
    score = X
    for i in range(N):
        if S[i] == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    print(score)

=======
Suggestion 7

def main():
    n,x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'o':
            x += 1
        elif s[i] == 'x' and x > 0:
            x -= 1
    print(x)

=======
Suggestion 8

def main():
    #n, x = map(int, input().split())
    #s = input()
    n, x = 20, 10
    s = 'xxxxxxxxxxxxxxxxxxxx'
    s = list(s)
    sum = x
    for i in range(n):
        if s[i] == 'o':
            sum += 1
        elif s[i] == 'x':
            if sum > 0:
                sum -= 1
    print(sum)
