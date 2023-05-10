Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    #input
    S = input()
    #S =

=======
Suggestion 2

def main():
    S = input()
    if len(set(S)) == 2:
        if S.count(S[0]) == 2 and S.count(S[1]) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    if len(set(s)) == 2 and s.count(s[0]) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def check(s):
    if len(set(s)) == 2:
        for i in set(s):
            if s.count(i) != 2:
                return False
        return True
    else:
        return False

=======
Suggestion 5

def main():
    s = input()
    if len(s) == 4:
        if len(set(s)) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input()
    if len(set(S)) == 2:
        if S.count(S[0]) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 7

def main():
    S = input()
    if len(set(S)) == 2 and S.count(S[0]) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    if len(set(s)) == 2 and s.count(s[0]) == 2:
        print('Yes')
    else:
        print('No')
