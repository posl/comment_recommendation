Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def answer(n, x, s):
    score = x
    for i in range(n):
        if s[i] == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    return score

=======
Suggestion 2

def main():
    N,X = map(int,input().split())
    S = input()
    for s in S:
        if s == "o":
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
    score = x
    for i in range(n):
        if s[i] == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    print(score)

=======
Suggestion 4

def main():
    n,x=map(int,input().split())
    s=input()
    for i in range(n):
        if s[i]=='o':
            x+=1
        else:
            if x>0:
                x-=1
    print(x)

=======
Suggestion 5

def countScore(N, X, S):
    score = X
    for i in range(N):
        if S[i] == 'o':
            score += 1
        elif S[i] == 'x' and score > 0:
            score -= 1
    return score

=======
Suggestion 6

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
Suggestion 7

def main():
    N, X = map(int, input().split())
    S = input()
    sum = X
    for i in range(N):
        if S[i] == 'o':
            sum += 1
        else:
            if sum > 0:
                sum -= 1
    print(sum)

=======
Suggestion 8

def check(s):
    return s.count('o')

n, x = map(int, input().split())
s = input()
print(x + check(s) - s.count('x'))

=======
Suggestion 9

def get_input():
    line1 = input().split(' ')
    line2 = input()
    return line1,line2
