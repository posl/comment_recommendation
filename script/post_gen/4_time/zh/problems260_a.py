Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    s1 = s[0]
    s2 = s[1]
    s3 = s[2]
    if s1 == s2:
        print(s3)
    elif s1 == s3:
        print(s2)
    elif s2 == s3:
        print(s1)
    else:
        print('-1')

=======
Suggestion 2

def find_uniq_char(s):
    if s[0] == s[1]:
        return s[2]
    elif s[0] == s[2]:
        return s[1]
    else:
        return s[0]

=======
Suggestion 3

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
Suggestion 4

def find_unique_char(string):
    ans = -1
    for i in range(len(string)):
        if string.rfind(string[i]) == i and string.find(string[i]) == i:
            ans = string[i]
            break
    return ans

=======
Suggestion 5

def func():
    s = input()
    if s[0] == s[1]:
        print(s[2])
    elif s[0] == s[2]:
        print(s[1])
    elif s[1] == s[2]:
        print(s[0])
    else:
        print(-1)

func()

=======
Suggestion 6

def main():
    s = input()
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            print(s[i])
            break
    else:
        print(-1)

=======
Suggestion 7

def get_str():
    return input()

=======
Suggestion 8

def func(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            print(s[i])
            return
    print("-1")

s = input()
func(s)

=======
Suggestion 9

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print(-1)
    elif s[0] == s[1]:
        print(s[2])
    elif s[1] == s[2]:
        print(s[0])
    elif s[0] == s[2]:
        print(s[1])
    else:
        print(-1)

=======
Suggestion 10

def main():
    S = input()

    if S[0] == S[1] and S[0] != S[2]:
        print(S[2])
    elif S[0] == S[2] and S[0] != S[1]:
        print(S[1])
    elif S[1] == S[2] and S[0] != S[1]:
        print(S[0])
    else:
        print(-1)
