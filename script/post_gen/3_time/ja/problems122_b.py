Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    S = S.replace('A','1')
    S = S.replace('C','1')
    S = S.replace('G','1')
    S = S.replace('T','1')
    S = S.replace('0','0')
    #print(S)
    S = S.split('0')
    #print(S)
    print(len(max(S)))

=======
Suggestion 2

def main():
    S = input()
    max = 0
    count = 0
    for i in range(len(S)):
        if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)

=======
Suggestion 3

def main():
    S = input()
    max = 0
    count = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            count += 1
            if max < count:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 4

def main():
    s = input()
    if len(s) == 1:
        if s == 'A' or s == 'C' or s == 'G' or s == 'T':
            print(1)
        else:
            print(0)
    else:
        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if 'A' in s[i:j] or 'C' in s[i:j] or 'G' in s[i:j] or 'T' in s[i:j]:
                    if count < len(s[i:j]):
                        count = len(s[i:j])
                else:
                    continue
        print(count)

=======
Suggestion 5

def main():
    s = input()
    max_len = 0
    current_len = 0
    for c in s:
        if c in 'ACGT':
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 0
    max_len = max(max_len, current_len)
    print(max_len)

=======
Suggestion 6

def main():
    S = input()
    ans = 0
    count = 0
    for i in range(len(S)):
        if S[i] in "ACGT":
            count += 1
            ans = max(ans, count)
        else:
            count = 0
    print(ans)

=======
Suggestion 7

def main():
    s = input()
    ans = 0
    now = 0
    for i in s:
        if i in "ACGT":
            now += 1
        else:
            now = 0
        ans = max(ans, now)
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    str = ""
    count = 0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
            str += s[i]
            count = max(count, len(str))
        else:
            str = ""
    print(count)

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i,n):
            if set(s[i:j+1]) <= set('ACGT'):
                ans = max(ans,j-i+1)
    print(ans)
main()

=======
Suggestion 10

def main():
    # 標準入力から文字列を取得
    S = input()
    # ACGT文字列の最大値を保持する変数
    max = 0
    # ACGT文字列の長さを保持する変数
    count = 0
    # ACGT文字列の最大値を保持する変数
    max = 0
    # ACGT文字列の長さを保持する変数
    count = 0
    # 文字列の長さ分ループ
    for i in range(len(S)):
        # 文字列がACGTの場合
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            # ACGT文字列の長さをインクリメント
            count += 1
        # 文字列がACGT以外の場合
        else:
            # ACGT文字列の最大値を保持する変数と比較
            if max < count:
                # ACGT文字列の最大値を保持する変数に代入
                max = count
            # ACGT文字列の長さを保持する変数を0に初期化
            count = 0
    # 最後の文字列がACGTの場合
    if max < count:
        # ACGT文字列の最大値を保持する変数に代入
        max = count
    # ACGT文字列の最大値を出力
    print(max)
