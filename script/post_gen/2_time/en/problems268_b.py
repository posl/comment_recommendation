Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T[0:len(S)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t[0:len(s)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if S == T[:len(S)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t[:len(s)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t[0:len(s)]:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if T.startswith(S):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s in t[:len(s)]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def isPrefix(s, t):
    if s == t:
        return True
    if len(s) > len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

=======
Suggestion 9

def check_prefix(s,t):
    if s == t[0:len(s)]:
        return "Yes"
    else:
        return "No"
