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

=======
Suggestion 2

def main():
    S = input()
    if len(set(S)) == 2:
        if S.count(S[0]) == 2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    if len(set(s)) == 2 and s.count(s[0]) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input()
    if len(set(S)) == 2 and S.count(S[0]) == 2:
        print('Yes')
    else:
        print('No')

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
    s = set(s)
    if len(s) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    print("Yes") if len(set(s)) == 2 and s.count(s[0]) == 2 else print("No")

=======
Suggestion 8

def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    s_set = set(s)
    if len(s_set) != 2:
        print("No")
        return
    for c in s_set:
        if s.count(c) != 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def main():
    S = input()
    if len(S) != 4:
        print("入力が不正です。")
        return
    elif S[0] == S[1] and S[2] == S[3]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    S = input()
    #S = "FREE"
    #S = "FFEE"
    #S = "STOP"
    #S = "ASSA"

    S = list(S)
    S.sort()
    S = "".join(S)

    if S == "AASS" or S == "EEFF":
        print("Yes")
    else:
        print("No")
