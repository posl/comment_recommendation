Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s.islower() or s.isupper():
        print('No')
    elif len(s) != len(set(s)):
        print('No')
    else:
        print('Yes')

=======
Suggestion 2

def main():
    S = input()
    if S.islower() or S.isupper():
        print("No")
    elif len(S) != len(set(S)):
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    s = input()
    if s.islower() or s.isupper() or len(s) != len(set(s)):
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    S = input()
    if S.islower() or S.isupper():
        print('No')
    else:
        if len(set(S)) == len(S):
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    S = input()
    if len(S) < 2:
        print('No')
        return
    if S.islower():
        print('No')
        return
    if S.isupper():
        print('No')
        return
    if len(S) != len(set(S)):
        print('No')
        return
    print('Yes')

=======
Suggestion 6

def main():
    s = input()
    if 'A' in s and 'a' in s:
        if len(set(s)) == len(s):
            print('Yes')
            return
    print('No')

=======
Suggestion 7

def main():
    S = input()

    if len(S) < 2:
        print("No")
        return

    if S.isupper():
        print("No")
        return

    if S.islower():
        print("No")
        return

    if S.isalpha() == False:
        print("No")
        return

    if len(S) != len(set(S)):
        print("No")
        return

    print("Yes")

=======
Suggestion 8

def main():
    S = input()
    if len(S) < 2:
        print("No")
        return

    if S.islower():
        print("No")
        return

    if S.isupper():
        print("No")
        return

    if not S.isalpha():
        print("No")
        return

    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if S[i] == S[j]:
                print("No")
                return

    print("Yes")

=======
Suggestion 9

def main():
    s = input()
    if s.isupper() or s.islower():
        print("No")
        return

    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                print("No")
                return
    print("Yes")

=======
Suggestion 10

def main():
    S = input()
    if len(S) < 2:
        print("No")
        return
    if S[0].isupper() and S[1].islower():
        for i in range(2, len(S)):
            if S[i].isupper():
                print("No")
                return
    else:
        print("No")
        return
    if len(set(S)) == len(S):
        print("Yes")
    else:
        print("No")
