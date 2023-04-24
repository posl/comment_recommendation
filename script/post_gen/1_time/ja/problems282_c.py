Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        if S[i] == '"':
            count += 1
        elif S[i] == ',' and count % 2 == 0:
            print('.', end='')
        else:
            print(S[i], end='')
    print()

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n):
        if s[i] == '"':
            count += 1
        if s[i] == ',' and count % 2 == 0:
            s = s[:i] + '.' + s[i+1:]
    print(s)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    ans = ""
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        elif S[i] == ',' and cnt % 2 == 0:
            ans += '.'
        else:
            ans += S[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    ans = ""
    cnt = 0
    for i in range(n):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',' and cnt % 2 == 0:
            ans += '.'
        else:
            ans += s[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    ans = ""
    count = 0
    for i in range(n):
        if s[i] == '"':
            count += 1
        elif s[i] == ',' and count % 2 == 0:
            ans += '.'
        else:
            ans += s[i]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    k = 0
    for i in range(n):
        if s[i] == '"':
            k += 1
        if s[i] == ',' and k % 2 == 0:
            s = s[:i] + '.' + s[i+1:]
    print(s)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    ans = ""
    flag = False
    for i in range(N):
        if S[i] == '"':
            flag = not flag
        elif S[i] == ',' and flag == False:
            ans += '.'
        else:
            ans += S[i]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    ans = ""
    flag = False
    for s in S:
        if s == '"':
            flag = not flag
        elif s == ',' and not flag:
            ans += '.'
        else:
            ans += s
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    i = 0
    while i < n:
        if s[i] == '"':
            i += 1
            while i < n and s[i] != '"':
                i += 1
        elif s[i] == ',':
            s = s[:i] + '.' + s[i+1:]
        i += 1
    print(s)
