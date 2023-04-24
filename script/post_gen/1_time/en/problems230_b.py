Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = 'oxx' * 10 ** 5
    if S in T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if s in 'o' * 10 ** 5:
        print('Yes')
    elif s in 'x' * 10 ** 5:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def is_substring(s):
    t = 'oxx' * 10**5
    return 'Yes' if s in t else 'No'

s = input()
print(is_substring(s))

=======
Suggestion 4

def isSubStr(s, t):
    for i in range(len(t) - len(s) + 1):
        if t[i:i+len(s)] == s:
            return True
    return False

s = input()
t = 'oxx' * 10**5

=======
Suggestion 5

def main():
    S = input()
    if S in 'o' * 10**5:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def is_substring(s):
    t = "oxx" * 100000
    return "Yes" if s in t else "No"

s = input()
print(is_substring(s))

=======
Suggestion 7

def main():
    S = input()
    L = len(S)
    if L > 10:
        print("No")
        return
    if L == 1:
        if S == "o":
            print("Yes")
        else:
            print("No")
        return
    if L == 2:
        if S == "ox" or S == "xo":
            print("Yes")
        else:
            print("No")
        return
    if L == 3:
        if S == "oxx" or S == "xox" or S == "xxo":
            print("Yes")
        else:
            print("No")
        return
    T = "oxx" + "xox" + "xxo"
    if L == 4:
        if S == T:
            print("Yes")
        else:
            print("No")
        return
    if L == 5:
        if S == T + "oxx" or S == T + "xox" or S == T + "xxo":
            print("Yes")
        else:
            print("No")
        return
    if L == 6:
        if S == T + "oxx" + "xox" or S == T + "xox" + "xxo" or S == T + "xxo" + "oxx":
            print("Yes")
        else:
            print("No")
        return
    if L == 7:
        if S == T + "oxx" + "xox" + "xxo" or S == T + "xox" + "xxo" + "oxx" or S == T + "xxo" + "oxx" + "xox":
            print("Yes")
        else:
            print("No")
        return
    if L == 8:
        if S == T + "oxx" + "xox" + "xxo" + "oxx" or S == T + "xox" + "xxo" + "oxx" + "xox" or S == T + "xxo" + "oxx" + "xox" + "xxo":
            print("Yes")
        else:
            print("No")
        return
    if L == 9:
        if S == T + "oxx" + "xox

=======
Suggestion 8

def main():
    # Read input
    S = input()
    # Check if S is a substring of T
    T = "oxx" * 100000
    if S in T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    S

=======
Suggestion 10

def is_substring(s):
    if 'o' not in s:
        return 'No'
    elif 'x' not in s:
        return 'Yes'
    elif 'x' not in s[0:s.find('o')]:
        return 'Yes'
    elif 'o' not in s[s.find('x'):]:
        return 'Yes'
    else:
        return 'No'

s = input()
print(is_substring(s))
