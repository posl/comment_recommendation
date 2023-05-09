Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == "L":
                print("No")
                return
        else:
            if s[i] == "R":
                print("No")
                return
    print("Yes")

=======
Suggestion 2

def main():
    s = input()
    for i in range(0, len(s), 2):
        if s[i] == 'L':
            print('No')
            return
    for i in range(1, len(s), 2):
        if s[i] == 'R':
            print('No')
            return
    print('Yes')

=======
Suggestion 3

def solve():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == 'L':
                return 'No'
        else:
            if S[i] == 'R':
                return 'No'
    return 'Yes'

print(solve())

=======
Suggestion 4

def main():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == 'L':
                print("No")
                return
        else:
            if S[i] == 'R':
                print("No")
                return
    print("Yes")

=======
Suggestion 5

def main():
    S = input()
    if S[::2].count('L') == 0 and S[1::2].count('R') == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    s = input()
    for i in range(len(s)):
        if (i+1) % 2 == 1:
            if s[i] == 'L':
                print('No')
                return
        else:
            if s[i] == 'R':
                print('No')
                return
    print('Yes')

=======
Suggestion 7

def main():
    s = input()
    if len(s) == 1:
        print('Yes')
        return
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                print('No')
                return
        else:
            if s[i] == 'R':
                print('No')
                return
    print('Yes')

=======
Suggestion 8

def solve():
    S = input().rstrip()
    if all([S[i] in 'RUD' for i in range(0, len(S), 2)]) and all([S[i] in 'LUD' for i in range(1, len(S), 2)]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    S = input()
    #print(S)
    for i in range(len(S)):
        if (i+1)%2 == 1:
            if S[i] in ['R','U','D']:
                pass
            else:
                print('No')
                return
        else:
            if S[i] in ['L','U','D']:
                pass
            else:
                print('No')
                return
    print('Yes')
    return
