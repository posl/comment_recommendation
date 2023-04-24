Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
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
    return

=======
Suggestion 2

def main():
    S = input()
    if S[::2].count('L') == 0 and S[1::2].count('R') == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0:
            if not s[i] in "RUD":
                print("No")
                return
        else:
            if not s[i] in "LUD":
                print("No")
                return
    print("Yes")

=======
Suggestion 4

def main():
    s = input()
    for i in range(len(s)):
        if (i + 1) % 2 == 1:
            if s[i] == "L":
                print("No")
                return
        else:
            if s[i] == "R":
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 5

def main():
    s = input()
    if len(s) == 1:
        if s == "R" or s == "U" or s == "D":
            print("Yes")
        else:
            print("No")
        return
    for i in range(1, len(s), 2):
        if s[i] == "R" or s[i] == "U" or s[i] == "D":
            continue
        else:
            print("No")
            return
    for i in range(0, len(s), 2):
        if s[i] == "L" or s[i] == "U" or s[i] == "D":
            continue
        else:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def solve():
    s = input()
    for i in range(len(s)):
        if (i % 2 == 1 and s[i] == 'L') or (i % 2 == 0 and s[i] == 'R'):
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def main():
    S = input()
    for i in range(len(S)):
        if i%2==0:
            if S[i] in ['L']:
                print('No')
                exit()
        else:
            if S[i] in ['R']:
                print('No')
                exit()
    print('Yes')

=======
Suggestion 8

def main():
    S = input()
    for i in range(len(S)):
        if (i+1)%2 == 1:
            if S[i] == "R":
                continue
            else:
                print("No")
                exit()
        else:
            if S[i] == "L":
                continue
            else:
                print("No")
                exit()
    print("Yes")

=======
Suggestion 9

def solve():
    # === 数値を取得 ===
    S = input()
    # === 文字列を取得 ===
    # === 行列を取得 ===
    # === 複数行の整数を取得 ===
    # === 複数行の文字列を取得 ===
    # === 複数行の行列を取得 ===
    # === 複数行の複数行の整数を取得 ===
    # === 複数行の複数行の文字列を取得 ===
    # === 複数行の複数行の行列を取得 ===
    # === 複数行の複数行の複数行の整数を取得 ===
    # === 複数行の複数行の複数行の文字列を取得 ===
    # === 複数行の複数行の複数行の行列を取得 ===
    # === 処理 ===
    for i in range(0, len(S)):
        if i % 2 == 0:
            if S[i] == "L":
                print("No")
                return
        else:
            if S[i] == "R":
                print("No")
                return
    print("Yes")

=======
Suggestion 10

def check(s):
    if len(s) == 0:
        return True
    if len(s) % 2 == 0:
        if s[0] not in ['L', 'U', 'D']:
            return False
        return check(s[1:])
    else:
        if s[0] not in ['R', 'U', 'D']:
            return False
        return check(s[1:])

S = input()
print('Yes' if check(S) else 'No')
