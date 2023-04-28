Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    K = int(input())

=======
Suggestion 2

def main():
    S = input()
    K = int(input())
    cnt = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            cnt += 1
    ans = min(cnt+2*K,len(S)-1)
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    k = int(input())
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'X':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(min(ans+k, len(s)))

=======
Suggestion 4

def main():
    s = input()
    k = int(input())
    l = len(s)
    cnt = 0
    for i in range(l-1):
        if s[i] == s[i+1]:
            cnt += 1
    ans = min(cnt + 2*k, l-1)
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    k = int(input())

    if len(s) == 1:
        print(0)
        return

    if k == 0:
        print(max([len(i) for i in s.split("X")]))
        return

    if "X" not in s:
        print(len(s))
        return

    s = s.replace("X", "X.")
    s = s.replace(".", ".X")
    s = s[1:-1]

    s = s.split(".")

    if len(s) == 1:
        print(len(s[0]))
        return

    if s[0] == "":
        s = s[1:]
    if s[-1] == "":
        s = s[:-1]

    if len(s) == 1:
        print(len(s[0]))
        return

    if len(s) == 2:
        print(max([len(s[0]), len(s[1])]))
        return

    if len(s) == 3:
        print(max([len(s[0]), len(s[1]), len(s[2])]))
        return

    if len(s) == 4:
        print(max([len(s[0]), len(s[1]), len(s[2]), len(s[3])]))
        return

    if len(s) == 5:
        print(max([len(s[0]), len(s[1]), len(s[2]), len(s[3]), len(s[4])]))
        return

=======
Suggestion 6

def main():
    s = input()
    k = int(input())
    if k == 0:
        print(max([len(i) for i in s.split('.')]))
    else:
        s = s.replace('X', '1').replace('.', '0')
        print(max([len(i) for i in s.split('0')]) + k)

=======
Suggestion 7

def main():
    S = input()
    K = int(input())

    # 答えを格納する変数
    ans = 0

    # 連続するXの数
    count = 0

    # 連続するXの数をカウント
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
        else:
            # XとXの間にある.の数を加算
            ans += count - 1 if count > 1 else 0
            count = 0

    # 最後のXとXの間にある.の数を加算
    ans += count - 1 if count > 1 else 0

    # K回操作を行う
    ans += K * 2

    # 答えを出力
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    K = int(input())
    if K == 0:
        print(S.count("X"))
        return
    #Sの先頭にXを追加
    S = "X" + S
    #Sの末尾にXを追加
    S = S + "X"
    #Sの連続したXの数をカウントする
    cnt = 0
    cnt_list = []
    for s in S:
        if s == "X":
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 0
    #print(cnt_list)
    #cnt_listの中の最大値を求める
    #cnt_listが空の場合は0を出力
    if len(cnt_list) == 0:
        print(0)
    else:
        print(max(cnt_list) + K)

=======
Suggestion 9

def main():
    S = input()
    K = int(input())
    X = S.replace('.', 'X')
    X = X.replace('X'*K, 'X')
    print(len(X))

=======
Suggestion 10

def main():
    s = input()
    k = int(input())

    #Xを最大で何個連続させられるか
    #Xの数を数える
    x_count = 0
    for i in range(len(s)):
        if s[i] == 'X':
            x_count += 1

    #Xをk回連続させる
    #Xの数がkより少ない場合はXの数を出力
    if x_count < k:
        print(x_count)
        return

    #Xの数がk以上の場合はkを出力
    print(k)
