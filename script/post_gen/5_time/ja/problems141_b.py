Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S[0::2].count("R") + S[0::2].count("U") + S[0::2].count("D") == len(S[0::2]) and S[1::2].count("L") + S[1::2].count("U") + S[1::2].count("D") == len(S[1::2]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def solve():
    s = input()
    for i in range(len(s)):
        if i%2 == 0:
            if s[i] == "L":
                return "No"
        else:
            if s[i] == "R":
                return "No"
    return "Yes"

=======
Suggestion 3

def main():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == 'L':
                print('No')
                return
        else:
            if S[i] == 'R':
                print('No')
                return
    print('Yes')

=======
Suggestion 4

def main():
    S = input()
    for i in range(0, len(S)):
        if i % 2 == 0 and S[i] == 'L':
            print('No')
            return
        if i % 2 == 1 and S[i] == 'R':
            print('No')
            return
    print('Yes')

=======
Suggestion 5

def main():
    s = input()
    for i in range(0, len(s), 2):
        if s[i] == 'L':
            print('No')
            exit()
    for i in range(1, len(s), 2):
        if s[i] == 'R':
            print('No')
            exit()
    print('Yes')
main()

=======
Suggestion 6

def main():
    s = input()
    s1 = s[0::2]
    s2 = s[1::2]
    if s1.count("R") == len(s1) and s2.count("L") == len(s2):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = input()
    l = len(s)
    for i in range(l):
        if i % 2 == 0:
            if s[i] == "L":
                print("No")
                exit()
        else:
            if s[i] == "R":
                print("No")
                exit()
    print("Yes")

=======
Suggestion 8

def main():
    S = input()
    N = len(S)
    for i in range(N):
        if i % 2 == 0:
            if S[i] == "L":
                print("No")
                return
        else:
            if S[i] == "R":
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 9

def solve(s):
    for i in range(len(s)):
        if i % 2 == 0 and s[i] in ['L', 'U', 'D']:
            continue
        elif i % 2 == 1 and s[i] in ['R', 'U', 'D']:
            continue
        else:
            return 'No'
    return 'Yes'

=======
Suggestion 10

def solve():
    S = input()
    for i in range(len(S)):
        if (i+1) % 2 == 0:
            if S[i] in ['L','U','D']:
                pass
            else:
                print('No')
                return
        else:
            if S[i] in ['R','U','D']:
                pass
            else:
                print('No')
                return
    print('Yes')
    return
