Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n = int(input())
    s = input()
    for i in range(n):
        if s[i] == '"':
            if i % 2 == 0:
                print('"', end='')
            else:
                print('.', end='')
        else:
            print(s[i], end='')
    print()

=======
Suggestion 2

def replace_string(s):
    s = list(s)
    for i in range(1,len(s)-1):
        if s[i] == ',' and s[i-1] == '"' and s[i+1] == '"':
            s[i] = '.'
    return ''.join(s)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    S = list(S)
    for i in range(1, N-1, 2):
        if S[i] == ',':
            S[i] = '.'
    print(''.join(S))

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    s_list = list(s)
    for i in range(0, n, 2):
        s_list[i] = '.'
    print(''.join(s_list))

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    s = list(s)
    for i in range(1, n+1):
        if i % 2 == 0:
            continue
        if s[i-1] != '"' and s[i] != '"':
            s[i-1] = '.'
    print(''.join(s))
main()

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    ans = ''
    for i in range(n):
        if i % 2 == 0:
            ans += s[i]
        else:
            if s[i] == '"':
                ans += '"'
            else:
                ans += '.'
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    for i in range(0,n,2):
        s = s.replace(s[i],'.')
    print(s)

=======
Suggestion 9

def replace(s):
    s = list(s)
    for i in range(len(s)):
        if i%2 == 1:
            s[i] = "."
    return "".join(s)
