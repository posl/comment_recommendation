Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T[:len(S)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if T.startswith(S):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    print("Yes" if t.startswith(s) else "No")

=======
Suggestion 6

def prefix(s, t):
    if s == t[:len(s)]:
        return 'Yes'
    else:
        return 'No'

s = input()
t = input()
print(prefix(s, t))

=======
Suggestion 7

def is_prefix(str1, str2):
    if str1[0:len(str1)] == str2[0:len(str1)]:
        return True
    else:
        return False

=======
Suggestion 8

def main():
    #read input
    S = input()
    T = input()
    #check if S is a prefix of T
    if T.startswith(S):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def prefix(S, T):
    if S == T[:len(S)]:
        return "Yes"
    return "No"

=======
Suggestion 10

def prefix(s, t):
    if t.startswith(s):
        return "Yes"
    return "No"
