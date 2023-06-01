Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    s = input()
    for i in range(3):
        if s.count(s[i]) == 1:
            print(s[i])
            return
    print(-1)

=======
Suggestion 2

def main():
    s = input()
    if s[0] == s[1]:
        print(s[2])
    elif s[0] == s[2]:
        print(s[1])
    elif s[1] == s[2]:
        print(s[0])
    else:
        print(-1)

=======
Suggestion 3

def main():
    S = input()
    for i in range(len(S)):
        if S.count(S[i]) == 1:
            print(S[i])
            break
    else:
        print('-1')

=======
Suggestion 4

def solve(string):
    for i in string:
        if string.count(i) == 1:
            return i
    return -1

print(solve(input()))

=======
Suggestion 5

def f(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s[i]
    return -1

s = input()
print(f(s))

=======
Suggestion 6

def single_char(str):
    if len(str) != 3:
        return -1
    else:
        if str[0] == str[1]:
            return str[2]
        elif str[0] == str[2]:
            return str[1]
        elif str[1] == str[2]:
            return str[0]
        else:
            return -1

=======
Suggestion 7

def solve():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print(-1)
    elif s[0] == s[1]:
        print(s[2])
    elif s[0] == s[2]:
        print(s[1])
    else:
        print(s[0])

solve()

=======
Suggestion 8

def solve():
    S = input()
    if S[0] == S[1]:
        print(S[2])
    elif S[0] == S[2]:
        print(S[1])
    elif S[1] == S[2]:
        print(S[0])
    else:
        print(-1)

=======
Suggestion 9

def func(s):
    for i in s:
        if s.count(i)==1:
            return i
    return -1

s=input()
print(func(s))

=======
Suggestion 10

def main():
    s = input()
    for c in s:
        if s.count(c) == 1:
            print(c)
            return
    print(-1)

main()
