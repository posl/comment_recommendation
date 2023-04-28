Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == "L":
                print("No")
                exit()
        else:
            if S[i] == "R":
                print("No")
                exit()
    print("Yes")

=======
Suggestion 2

def main():
    s = input()
    if s[::2].count("L") == 0 and s[1::2].count("R") == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0 and S[i] == "L":
            print("No")
            return
        elif i % 2 == 1 and S[i] == "R":
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    s = input()
    for i in range(len(s)):
        if (i+1)%2 == 1:
            if s[i] == "R" or s[i] == "U" or s[i] == "D":
                continue
            else:
                print("No")
                return
        else:
            if s[i] == "L" or s[i] == "U" or s[i] == "D":
                continue
            else:
                print("No")
                return
    print("Yes")

=======
Suggestion 5

def solve():
    # ===CODE===
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == "L":
                return "No"
        else:
            if S[i] == "R":
                return "No"
    return "Yes"

=======
Suggestion 6

def main():
    s = input()
    if len(s) % 2 == 0:
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == 'L':
                    print('No')
                    exit()
            else:
                if s[i] == 'R':
                    print('No')
                    exit()
    else:
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == 'R':
                    print('No')
                    exit()
            else:
                if s[i] == 'L':
                    print('No')
                    exit()
    print('Yes')

=======
Suggestion 7

def solve():
    # === 数値を取得 ===
    # N = int(input())
    S = input()

    # === 文字列を取得 ===
    # S = input()

    # === 処理 ===
    for i in range(0, len(S), 2):
        if S[i] not in ['R', 'U', 'D']:
            print('No')
            return

    for i in range(1, len(S), 2):
        if S[i] not in ['L', 'U', 'D']:
            print('No')
            return

    print('Yes')

=======
Suggestion 8

def is_easy(s):
    for i in range(len(s)):
        if i % 2 == 0 and s[i] in ['L', 'U', 'D']:
            continue
        elif i % 2 == 1 and s[i] in ['R', 'U', 'D']:
            continue
        else:
            return False
    return True

s = input()

=======
Suggestion 9

def main():
    s = input()
    s1 = s[::2]
    s2 = s[1::2]
    if s1.count('L') + s2.count('R') + s1.count('U') + s2.count('D') == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    s = str(input())
    s = list(s)
    flag = True
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == "L":
                flag = False
        else:
            if s[i] == "R":
                flag = False
    if flag:
        print("Yes")
    else:
        print("No")
