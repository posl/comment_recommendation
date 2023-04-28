Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 3

def main():
    s = input()
    t = input()
    flag = False
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def solve():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            return "Yes"
    return "No"

print(solve())

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    for i in range(0, len(s)):
        if s == t:
            print("Yes")
            return
        else:
            s = s[-1] + s[:-1]
    print("No")

main()

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def solve():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            return "No"
    return "Yes"

print(solve())

=======
Suggestion 9

def solve():
    s = input()
    t = input()
    s = s + s
    if t in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def solve(s, t):
    if s == t:
        return True
    else:
        return False
