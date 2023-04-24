Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        print("Yes")
    elif s[0] == s[2] and s[1] == s[3] and s[0] != s[1]:
        print("Yes")
    elif s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    S = input()
    if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
        print('Yes')
    elif S[0] == S[2] and S[1] == S[3] and S[0] != S[1]:
        print('Yes')
    elif S[0] == S[3] and S[1] == S[2] and S[0] != S[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        print('Yes')
    elif s[0] == s[2] and s[1] == s[3] and s[0] != s[1]:
        print('Yes')
    elif s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input()
    if S[0] == S[1] and S[1] != S[2] and S[2] == S[3]:
        print("Yes")
    elif S[0] == S[1] and S[1] == S[2] and S[2] != S[3]:
        print("Yes")
    elif S[0] != S[1] and S[1] == S[2] and S[2] == S[3]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def check(s):
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        return "Yes"
    elif s[0] == s[2] and s[1] == s[3] and s[0] != s[1]:
        return "Yes"
    elif s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
        return "Yes"
    else:
        return "No"

=======
Suggestion 6

def check(s):
    if len(s) != 4:
        return False
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        return True
    elif s[0] == s[2] and s[1] == s[3] and s[0] != s[1]:
        return True
    elif s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
        return True
    else:
        return False

s = input()

=======
Suggestion 7

def main():
    s = input()
    print("Yes" if len(set(s)) == 2 and s.count(s[0]) == 2 else "No")

=======
Suggestion 8

def main():
    s = input()
    if len(set(s)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    S = input()
    print('Yes' if len(set(S)) == 2 and S.count(S[0]) == 2 else 'No')

=======
Suggestion 10

def main():
    s = input()
    if len(set(s)) != 2:
        print("No")
    else:
        print("Yes")
