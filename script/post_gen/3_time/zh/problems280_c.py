Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break

=======
Suggestion 2

def solve():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(s)+1)
    return 0

=======
Suggestion 3

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(s)+1)

=======
Suggestion 4

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i + 1)
            return
    print(len(s) + 1)

=======
Suggestion 5

def solve():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(s)+1)

=======
Suggestion 6

def solve(s, t):
    for i in range(len(s)):
        if s[:i] + s[i+1:] == t:
            return i+1
    return len(s)+1

=======
Suggestion 7

def find_diff(s, t):
    for i in range(len(t)):
        if s[i] != t[i]:
            return i
    return len(t)

=======
Suggestion 8

def main():
    s = input()
    t = input()
    for i in range(0, len(s)):
        if s[i] != t[i]:
            print(i + 1)
            break
