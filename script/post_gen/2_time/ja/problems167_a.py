Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t[:-1] == s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()

    if S == T[:-1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s + 'z' == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    # 入力
    s = input()
    t = input()
    # 処理
    if s == t[:-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    S = input() #ID
    T = input() #新しいID

    if S == T[0:len(S)] and len(T) == len(S) + 1:
        print("Yes")
    else:
        print("No")
