Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[2] == s[3] and s[4] == s[5]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    if S[2] == S[3] and S[4] == S[5]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def is_coffee(s):
    if len(s) != 6:
        return False
    if s[2] == s[3] and s[4] == s[5]:
        return True
    return False

=======
Suggestion 4

def is_coffee(s):
    if s[2] == s[3] and s[4] == s[5]:
        return True
    else:
        return False

s = input()
