Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    for i in range(len(S)):
        if i%2 == 0:
            if S[i] == 'L':
                print('No')
                exit()
        else:
            if S[i] == 'R':
                print('No')
                exit()
    print('Yes')

=======
Suggestion 2

def main():
    s = input()
    result = 'Yes'
    for i in range(len(s)):
        if (i % 2 == 0 and s[i] == 'L') or (i % 2 == 1 and s[i] == 'R'):
            result = 'No'
            break
    print(result)

=======
Suggestion 3

def main():
    S = input()
    if all([S[i] in 'RUD' for i in range(len(S)) if i % 2 == 0]) and all([S[i] in 'LUD' for i in range(len(S)) if i % 2 == 1]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input()
    if (S[::2].find('L') == -1 and S[1::2].find('R') == -1):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    for i, c in enumerate(s):
        if i % 2 == 0 and c in ['L']:
            print('No')
            return
        elif i % 2 == 1 and c in ['R']:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 6

def main():
    # input
    S = input()

    # compute

    # output
    if S[0::2].count('L') + S[0::2].count('R') + S[1::2].count('U') + S[1::2].count('D') == len(S):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    for i in range(0, len(s)):
        if (i % 2 == 0) and (s[i] == 'L'):
            print("No")
            return
        if (i % 2 == 1) and (s[i] == 'R'):
            print("No")
            return
    print("Yes")

=======
Suggestion 8

def main():
    S = input()
    for i in range(len(S)):
        if i%2 == 0:
            if S[i] in ['L','D']:
                print('No')
                return
        else:
            if S[i] in ['R','D']:
                print('No')
                return
    print('Yes')
    return

=======
Suggestion 9

def main():
    s = input()
    if s[0] == 'L' or s[1] == 'L':
        print('No')
    elif s[0] == 'R' and s[1] == 'R':
        print('No')
    elif s[0] == 'U' and s[1] == 'D':
        print('No')
    elif s[0] == 'D' and s[1] == 'U':
        print('No')
    elif s[0] == 'U' and s[1] == 'U':
        print('No')
    elif s[0] == 'D' and s[1] == 'D':
        print('No')
    elif s[0] == 'L' and s[1] == 'R':
        print('No')
    elif s[0] == 'R' and s[1] == 'L':
        print('No')
    else:
        print('Yes')

=======
Suggestion 10

def main():
    s = input()
    if len(s) == 1:
        print("Yes")
        return
    if len(s) % 2 == 0:
        print("Yes" if s[::2].count("L") == 0 and s[1::2].count("R") == 0 else "No")
    else:
        print("No")
