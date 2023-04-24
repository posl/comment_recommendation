Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if 'A' in s and 'a' in s and len(set(s)) == len(s):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if s.isupper() or s.islower():
        print("No")
    elif len(set(s)) == len(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    if S.isupper() or S.islower():
        print("No")
        return
    if len(S) != len(set(S)):
        print("No")
        return
    print("Yes")

=======
Suggestion 4

def main():
    s = input()
    a = 0
    b = 0
    for i in s:
        if i.isupper():
            a = 1
        if i.islower():
            b = 1
    if a == 1 and b == 1 and len(set(s)) == len(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    S = input()
    if len(S) >= 2 and len(S) <= 100:
        if S.islower() or S.isupper():
            print('No')
        else:
            if len(set(S)) == len(S):
                print('Yes')
            else:
                print('No')
    else:
        print('No')

=======
Suggestion 6

def main():
    S = input()
    if len(S) >= 1 and len(S) <= 100:
        if S.isupper() and S.islower():
            print("No")
        elif S.isupper():
            print("No")
        elif S.islower():
            print("No")
        else:
            if len(S) == len(set(S)):
                print("Yes")
            else:
                print("No")
    else:
        print("No")

=======
Suggestion 7

def main():
    S = input()
    S = S.lower()
    S = list(set(S))
    if len(S) == 26:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    S = input()
    if len(S) < 2 or len(S) > 100:
        print("入力エラー")
        return
    if S.islower() or S.isupper():
        print("No")
        return
    if S.isalpha() == False:
        print("入力エラー")
        return
    if len(set(S)) != len(S):
        print("No")
        return
    print("Yes")

=======
Suggestion 9

def main():
    S = input()
    if len(set(S)) != len(S) or S.islower():
        print('No')
    else:
        print('Yes')

=======
Suggestion 10

def main():
    # 入力
    S = input()

    # 処理
    flg = True
    for i in range(len(S)):
        if S[i].isupper():
            for j in range(len(S)):
                if S[j].islower():
                    for k in range(len(S)):
                        if S[i] == S[j] or S[i] == S[k] or S[j] == S[k]:
                            flg = False
                            break
    # 出力
    if flg:
        print("Yes")
    else:
        print("No")
