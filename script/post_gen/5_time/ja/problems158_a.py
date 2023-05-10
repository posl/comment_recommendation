Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s.count('A') == 1 and s.count('B') == 2:
        print('Yes')
    elif s.count('A') == 2 and s.count('B') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    s = input()
    if s.count("A") == 1:
        print("Yes")
    elif s.count("B") == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    if s.count('A')==1 and s.count('B')==2:
        print('Yes')
    elif s.count('B')==1 and s.count('A')==2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    if s.count('A') == 1 and s.count('B') == 2 or s.count('A') == 2 and s.count('B') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    S = input()
    if S[0] == S[1] == S[2]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    S = input()
    if S.count('A') == 1 or S.count('B') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 9

def solve():
    # === 数値変数の入力 ===
    # N = int(input())  # 1つの整数
    # L, R = map(int, input().split())  # 複数の整数
    # a = list(map(int, input().split()))  # 複数の整数
    S = input()  # 1つの文字列
    # === 行列の入力 ===
    # A = []
    # for i in range(N):
    #     A.append(list(map(int, input().split())))  # 複数の整数(スペース区切り)を受け取る
    # A = [list(map(int, input().split())) for i in range(N)]  # 複数の整数(スペース区切り)を受け取る

    # ここに書く
    if S[0] == S[1] == S[2]:
        print("No")
    else:
        print("Yes")
