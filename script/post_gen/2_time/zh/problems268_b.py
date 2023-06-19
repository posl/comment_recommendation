Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t[0:len(s)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t[0:len(s)]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def is_prefix(s,t):
    if len(s) > len(t):
        return 'No'
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                return 'No'
        return 'Yes'

s = input()
t = input()
print(is_prefix(s,t))

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if t[0:len(s)] == s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if len(s) > len(t):
        print("No")
    else:
        if s == t[:len(s)]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def isPrefix(s, t):
    if len(s) > len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

S = input()
T = input()
