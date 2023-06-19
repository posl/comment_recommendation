Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def isSubString(s,t):
    if len(s) < len(t):
        return False
    if s == t:
        return True
    if t in s:
        return True
    else:
        return False

=======
Suggestion 2

def check_string(s, t):
    if len(t) > len(s):
        return False
    if t in s:
        return True
    else:
        return False

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t in s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if t in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def solve():
    S = input()
    T = input()
    if T in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print("No")
        return
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if T in S:
        print("Yes")
    else:
        print("No")
