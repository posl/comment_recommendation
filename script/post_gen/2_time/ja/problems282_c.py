Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',' and cnt % 2 == 1:
            s = s[:i] + '.' + s[i+1:]
    print(s)

=======
Suggestion 2

def main():
    N = int(input())
    S = list(input())
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        if S[i] == ',' and cnt % 2 == 0:
            S[i] = '.'
    print(''.join(S))

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        if S[i] == '"':
            count += 1
        elif S[i] == ',' and count % 2 == 1:
            S = S[:i] + '.' + S[i+1:]
    print(S)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        if S[i] == '"':
            count += 1
        if S[i] == ',' and count % 2 == 0:
            S = S[:i] + '.' + S[i+1:]
    print(S)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',':
            if cnt % 2 == 0:
                print('.', end = '')
            else:
                print(',', end = '')
        else:
            print(s[i], end = '')
    print()

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    ans = ''
    cnt = 0
    for i in range(n):
        if s[i] == '"':
            cnt += 1
        if s[i] == ',' and cnt % 2 == 1:
            ans += '.'
        else:
            ans += s[i]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    ans = ""
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
            if cnt % 2 == 0:
                ans += '"'
            else:
                ans += '"'
        elif S[i] == ',':
            if cnt % 2 == 0:
                ans += ','
            else:
                ans += '.'
        else:
            ans += S[i]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()

    c = 0
    for i in range(N):
        if S[i] == '"':
            c += 1
        if S[i] == ',' and c % 2 == 0:
            S = S[:i] + '.' + S[i+1:]
    print(S)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    ans = ""
    flag = 0
    for i in range(N):
        if S[i] == '"':
            flag += 1
        elif S[i] == ',' and flag % 2 == 1:
            ans += S[i]
        else:
            ans += "."
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    S = input()

    if N == 1:
        print(S)
    else:
        for i in range(N):
            if i % 2 == 1 and S[i] == ',':
                print('.',end='')
            else:
                print(S[i],end='')
        print()
