Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    s = s + s
    if t in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def rotate(s):
    return s[1:] + s[0]

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s in t+t:
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 4

def rotate(s):
    return s[-1] + s[:-1]

s = input()
t = input()

=======
Suggestion 5

def rotate(s):
    return s[-1] + s[:-1]

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s == t:
            print("Yes")
            return
        s = s[-1] + s[:-1]
    print("No")

=======
Suggestion 7

def judge(s,t):
    if s == t:
        return True
    else:
        return False

=======
Suggestion 8

def check(s,t):
    if len(s) != len(t):
        return False
    if s == t:
        return True
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            return True
    return False

=======
Suggestion 9

def solve():
    s = input()
    t = input()
    if s in t*2:
        print("Yes")
    else:
        print("No")
