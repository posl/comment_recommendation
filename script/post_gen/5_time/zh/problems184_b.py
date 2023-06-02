Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    s = input()
    score = x
    for i in range(n):
        if s[i] == 'o':
            score += 1
        elif s[i] == 'x' and score > 0:
            score -= 1
    print(score)

=======
Suggestion 2

def main():
    n,x = map(int,input().split())
    s = input()
    count = x
    for i in s:
        if i == 'o':
            count += 1
        else:
            if count == 0:
                continue
            else:
                count -= 1
    print(count)

=======
Suggestion 3

def solve(n,x,s):
    score = x
    for i in range(n):
        if s[i] == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    return score

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
    n,x=input().split()
    n=int(n)
    x=int(x)
    s=input()
    sum=x
    for i in range(n):
        if s[i]=='o':
            sum+=1
        elif s[i]=='x' and sum>0:
            sum-=1
    print(sum)

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'x':
            if ans > 0:
                ans -= 1
        else:
            ans += 1
    print(ans)
main()

=======
Suggestion 7

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
Suggestion 8

def main():
    N,X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'o':
            X += 1
        elif S[i] == 'x' and X > 0:
            X -= 1
    print(X)

=======
Suggestion 9

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
