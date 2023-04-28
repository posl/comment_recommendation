Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    s = input()
    if len(set(s)) == 2 and s.count(s[0]) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def solve():
    S = input()
    if len(set(S)) == 2:
        if S.count(S[0]) == 2 and S.count(S[1]) == 2:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 4

def main():
    S = input()
    count = 0
    for i in S:
        if S.count(i) == 2:
            count += 1
    if count == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S = input()
    if len(set(S)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    if len(set(s)) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def isSameChar(str):
    if str[0] == str[1] and str[2] == str[3] and str[0] != str[2]:
        return True
    elif str[0] == str[2] and str[1] == str[3] and str[0] != str[1]:
        return True
    elif str[0] == str[3] and str[1] == str[2] and str[0] != str[1]:
        return True
    else:
        return False

=======
Suggestion 8

def main():
    s = input()
    if len(set(list(s))) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def solve():
    S = input()
    if len(set(S)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    S = input()
    print("Yes" if len(set(S)) == 2 else "No")
