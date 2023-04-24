Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        print("Yes")
    elif s[0] == s[2] and s[1] == s[3] and s[0] != s[1]:
        print("Yes")
    elif s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    S = sorted(S)
    if S[0] == S[1] and S[2] == S[3] and S[1] != S[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    if len(S) == 4 and len(set(S)) == 2 and S.count(S[0]) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input()
    S = list(S)
    S.sort()
    if S[0] == S[1] and S[2] == S[3]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("No")
        return
    if s[0] == s[1] and s[2] == s[3]:
        print("Yes")
        return
    if s[0] == s[2] and s[1] == s[3]:
        print("Yes")
        return
    if s[0] == s[3] and s[1] == s[2]:
        print("Yes")
        return
    print("No")

=======
Suggestion 6

def main():
    s = input()
    if len(set(s)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    S = input()
    #print(S)
    if S.count(S[0]) == 2 and S.count(S[1]) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    if len(s) != 4:
        return
    if s[0] == s[1] == s[2] == s[3]:
        return
    if s[0] == s[1] and s[2] == s[3]:
        print("Yes")
    elif s[0] == s[2] and s[1] == s[3]:
        print("Yes")
    elif s[0] == s[3] and s[1] == s[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    S = input()
    # S = "ASSA"
    # S = "STOP"
    # S = "FFEE"
    # S = "FREE"

    if len(S) == 4:
        if len(set(S)) == 2:
            if S.count(S[0]) == 2 and S.count(S[2]) == 2:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 10

def main():
    S = input()
    # 文字列の重複を削除
    S = list(set(S))
    # 文字列の重複を削除した結果が2つの場合
    if len(S) == 2:
        print('Yes')
    else:
        print('No')
