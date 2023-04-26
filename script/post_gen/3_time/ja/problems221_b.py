Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    if count == 2 or count == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        count = 0
        for i in range(len(S)):
            if S[i] != T[i]:
                count += 1
        if count == 2:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)-1):
        if s[:i] + s[i+1] + s[i] + s[i+2:] == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        S = S[:i] + S[i+1] + S[i] + S[i+2:]
        if S == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(len(s)-1):
        tmp = list(s)
        tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
        if ''.join(tmp) == t:
            print('Yes')
            return
    print('No')

=======
Suggestion 6

def main():
    S = input()
    T = input()

    if S == T:
        print('Yes')
        return

    for i in range(len(S)-1):
        tmp = list(S)
        tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
        if ''.join(tmp) == T:
            print('Yes')
            return

    print('No')

=======
Suggestion 7

def main():
    S = input()
    T = input()
    ans = "No"
    for i in range(len(S)):
        if S == T:
            ans = "Yes"
            break
        S = S[1:] + S[0]
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S) - 1):
            if S[i] == T[i] and S[i + 1] == T[i + 1]:
                print('Yes')
                return
            if S[i] == T[i + 1] and S[i + 1] == T[i]:
                print('Yes')
                return
        print('No')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    ans = 'Yes'
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i+1:] == t[i+1:]:
                print(ans)
                return
            else:
                ans = 'No'
    print(ans)

=======
Suggestion 10

def main():
    S = input()
    T = input()
    # 文字列の長さを取得
    str_len = len(S)
    # 文字列の長さ分ループ
    for i in range(str_len):
        # 1文字目と2文字目を入れ替える
        S = S[1:] + S[0]
        # 入れ替えた文字列とTが一致しているか確認
        if S == T:
            print("Yes")
            exit()
    # 1文字目と2文字目を入れ替えても一致しなかった場合
    print("No")
