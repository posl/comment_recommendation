Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
        print("Yes")
    elif S[0] == S[2] and S[1] == S[3] and S[0] != S[1]:
        print("Yes")
    elif S[0] == S[3] and S[1] == S[2] and S[0] != S[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

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
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] and s[2] == s[3]:
        if s[0] != s[2]:
            print("Yes")
        else:
            print("No")
    elif s[0] == s[2] and s[1] == s[3]:
        if s[0] != s[1]:
            print("Yes")
        else:
            print("No")
    elif s[0] == s[3] and s[1] == s[2]:
        if s[0] != s[1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    if len(set(s)) == 2:
        if s.count(s[0]) == 2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

main()

=======
Suggestion 5

def main():
    S = input()
    S = sorted(S)
    if S[0] == S[1] and S[2] == S[3] and S[1] != S[2]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    s = input()
    if len(set(s)) == 2:
        if s.count(s[0]) == 2 and s.count(s[1]) == 2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    if len(set(s)) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s = input()
    a = []
    for i in s:
        if i not in a:
            a.append(i)
    if len(a) == 2:
        for i in a:
            if s.count(i) == 2:
                print("Yes")
            else:
                print("No")
                break
    else:
        print("No")
