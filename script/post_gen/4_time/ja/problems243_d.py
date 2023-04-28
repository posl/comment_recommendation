Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == "U":
            x //= 2
        elif s[i] == "L":
            x = 2 * x - 1
        else:
            x = 2 * x + 1
    print(x)
main()

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans = ans // 2
        elif s[i] == 'L':
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    print(ans)

=======
Suggestion 3

def main():
    n,x = map(int,input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == "U":
            ans //= 2
        elif s[i] == "L":
            ans = ans * 2 - 1
        else:
            ans = ans * 2 + 1
    print(ans)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'L':
            ans = ans * 2
        elif s[i] == 'R':
            ans = ans * 2 + 2
        else:
            ans = ans * 2 + 1
    print(ans)

=======
Suggestion 5

def main():
    N,X = map(int,input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == "U":
            ans = ans//2
        elif S[i] == "L":
            ans = ans*2
        elif S[i] == "R":
            ans = ans*2+1
    print(ans)

=======
Suggestion 6

def readinput():
    n,x=input().split()
    s=input()
    n=int(n)
    x=int(x)
    return n,x,s

=======
Suggestion 7

def move(x, s):
    if s == 'U':
        return x // 2
    elif s == 'L':
        return x * 2
    elif s == 'R':
        return x * 2 + 1
    else:
        return x

=======
Suggestion 8

def move(s, x):
    if s == 'U':
        return x // 2
    elif s == 'L':
        return x * 2
    else:
        return x * 2 + 1

n, x = map(int, input().split())
s = input()

for i in range(n):
    x = move(s[i], x)

print(x)

=======
Suggestion 9

def calc_next_pos(pos, move):
    if move == "U":
        return pos // 2
    elif move == "L":
        return pos * 2
    elif move == "R":
        return pos * 2 + 1
    else:
        assert False

=======
Suggestion 10

def move(n, s, x):
    if n == 0:
        return x
    if s[n-1] == 'U':
        return move(n-1, s, x//2)
    elif s[n-1] == 'L':
        return move(n-1, s, x//2)
    else:
        return move(n-1, s, x//2+1)
