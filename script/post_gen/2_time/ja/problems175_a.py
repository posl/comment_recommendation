Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S == 'RRR':
        print(3)
    elif S == 'RRS' or S == 'SRR':
        print(2)
    elif S == 'SSS':
        print(0)
    else:
        print(1)

=======
Suggestion 2

def main():
    s = input()
    if s == 'RRR':
        print(3)
    elif s == 'RRS' or s == 'SRR':
        print(2)
    elif s == 'SSS':
        print(0)
    else:
        print(1)

=======
Suggestion 3

def main():
    S = input()
    if S == "RRR":
        print(3)
    elif S[0:2] == "RR" or S[1:3] == "RR":
        print(2)
    elif S[0] == "R" or S[1] == "R" or S[2] == "R":
        print(1)
    else:
        print(0)

=======
Suggestion 4

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'R':
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

=======
Suggestion 5

def main():
    S = input()
    cnt = 0
    max_cnt = 0
    for i in range(3):
        if S[i] == "R":
            cnt += 1
        else:
            cnt = 0
        if cnt > max_cnt:
            max_cnt = cnt
    print(max_cnt)

=======
Suggestion 6

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(3):
        if S[i] == 'R':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 7

def main():
    S = input()
    count = 0
    max = 0
    for i in range(3):
        if S[i] == 'R':
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 8

def main():
    S = input()

    cnt = 0
    max_cnt = 0
    for s in S:
        if s == 'R':
            cnt += 1
            max_cnt = max(cnt, max_cnt)
        else:
            cnt = 0

    print(max_cnt)

=======
Suggestion 9

def main():
    # 文字列の入力
    S = input()
    # 雨の日数
    R_count = 0
    # 雨の日数の最大値
    R_max = 0
    # 文字列の文字を取り出す
    for s in S:
        # 文字が雨の日の場合
        if s == 'R':
            # 雨の日数をカウントアップ
            R_count += 1
        # 文字が雨の日ではない場合
        else:
            # 雨の日数の最大値を更新
            R_max = max(R_count, R_max)
            # 雨の日数をリセット
            R_count = 0
    # 最後の日の雨の日数の最大値を更新
    R_max = max(R_count, R_max)
    # 雨の日数の最大値を出力
    print(R_max)
