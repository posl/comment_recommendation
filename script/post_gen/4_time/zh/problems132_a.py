Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if len(S) != 4:
        print('No')
        return
    if len(set(S)) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    s = s.upper()
    if len(s) != 4:
        print("No")
        return
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        print("Yes")
    elif s[0] == s[2] and s[1] == s[3] and s[0] != s[1]:
        print("Yes")
    elif s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    a = s[0]
    b = s[1]
    c = s[2]
    d = s[3]
    if((a == b and c == d and b != c) or (a == c and b == d and b != c) or (a == d and b == c and b != d)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    if len(set(s)) == 2 and s.count(s[0]) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def judge(s):
    if len(s) != 4 or not s.isupper():
        return False
    else:
        for i in range(4):
            if s.count(s[i]) != 2:
                return False
        return True

=======
Suggestion 6

def main():
    S = input()
    S_list = list(S)
    S_set = set(S_list)
    if len(S_set) == 2:
        for i in S_set:
            if S_list.count(i) != 2:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")

=======
Suggestion 7

def is2char(s):
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

=======
Suggestion 8

def main():
    s = input()
    if len(set(s)) == 2 and s.count(s[0]) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    s=input()
    if s[0]==s[1] and s[2]==s[3] and s[0]!=s[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    if len(set(s)) == 2:
        print("Yes")
    else:
        print("No")
