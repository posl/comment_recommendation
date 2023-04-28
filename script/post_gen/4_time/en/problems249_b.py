Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s.islower() or s.isupper():
        print("No")
    else:
        if len(set(s)) == len(s):
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    s = input()
    if s.islower() or s.isupper():
        print('No')
    elif len(set(s)) == len(s):
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 3

def main():
    S = input()
    if len(S) < 2:
        print("No")
    elif len(S) == 2:
        if S[0] == S[1]:
            print("No")
        else:
            print("Yes")
    else:
        if S[0].islower() or S[1].islower():
            print("No")
        else:
            for i in range(2, len(S)):
                if S[i].islower():
                    print("No")
                    exit(0)
            print("Yes")

=======
Suggestion 4

def main():
    s = input()
    if s.islower() or s.isupper():
        print("No")
    else:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                print("No")
                break
        else:
            print("Yes")

main()

=======
Suggestion 5

def main():
    s = input()
    if len(s) < 2:
        print("No")
        return
    if s.islower() or s.isupper():
        print("No")
        return
    if len(set(s)) != len(s):
        print("No")
        return
    print("Yes")

=======
Suggestion 6

def is_wonderful(s):
    return len(s) == len(set(s)) and s.lower() != s and s.upper() != s

s = input()
print("Yes" if is_wonderful(s) else "No")

=======
Suggestion 7

def is_wonderful_string(S):
    if len(S) < 2:
        return False
    if S.islower() or S.isupper():
        return False
    if len(S) != len(set(S)):
        return False
    return True

S = input()

=======
Suggestion 8

def main():
    s = input()
    if s.lower() == s or s.upper() == s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    s = input()
    if len(s) >= 2:
        if s.isupper():
            print("No")
        elif s.islower():
            print("No")
        elif s.isalpha():
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 10

def main():
    s = input()
    print("Yes" if s.islower() or s.isupper() else "No")
