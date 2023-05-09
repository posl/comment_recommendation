Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    for i in range(n):
        if s[i] == "," and i%2 == 1:
            print(".", end="")
        else:
            print(s[i], end="")
    print()

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    for i in range(n):
        if s[i] == ',':
            if (i+1) % 2 == 0:
                s = s[:i] + '.' + s[i+1:]
    print(s)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    s = s.split('"')
    for i in range(1, len(s), 2):
        s[i] = s[i].replace(',', '.')
    print('"'.join(s))

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    K = int(S.count('"')/2)
    for i in range(1,K+1):
        S = S.replace(',', '.', 1)
    print(S)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    print(s.replace(',', '.') if s.count('"') % 2 == 0 else s)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        if S[i] == ',':
            if cnt % 2 == 0:
                ans[i] = 1
    for i in range(N):
        if ans[i] == 1:
            print('.', end='')
        else:
            print(S[i], end='')
    print()

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    s1 = s.replace(',','.')
    s2 = s1.split('"')
    for i in range(len(s2)):
        if i%2 == 1:
            s2[i] = s2[i].replace('.','"')
    s3 = '"'.join(s2)
    print(s3)

=======
Suggestion 8

def replace_comma(S):
    S = list(S)
    K = S.count('"') // 2
    for i in range(1, K + 1):
        start = S.index('"')
        end = S.index('"', start + 1)
        for j in range(start, end + 1):
            if S[j] == ',':
                S[j] = '.'
    return "".join(S)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    S = S.replace(',', '.')
    S = S.replace('"', ',')
    print(S)
