Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    count = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    cnt0 = 0
    cnt1 = 0
    for i in range(n):
        if i % 2 == 0:
            if s[i] == '1':
                cnt0 += 1
            else:
                cnt1 += 1
        else:
            if s[i] == '1':
                cnt1 += 1
            else:
                cnt0 += 1
    print(min(cnt0, cnt1))

=======
Suggestion 3

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    if n == 1:
        print(0)
        return
    if n == 2:
        if s[0] == s[1]:
            print(1)
        else:
            print(0)
        return

    # 連続する0の数
    zero = 0
    # 連続する1の数
    one = 0
    for i in range(n):
        if s[i] == "0":
            zero += 1
        else:
            one += 1

    print(min(zero, one))

main()

=======
Suggestion 5

def main():
    # 入力
    S = input()
    # 0と1の数を数える
    S0 = S.count('0')
    S1 = S.count('1')
    # 出力
    print(min(S0, S1))

=======
Suggestion 6

def main():
    S = input()
    #S = '000'
    #S = '10010010'
    #S = '0'
    print(S)

=======
Suggestion 7

def main():
    S = input()
    # 0と1の数を数える
    c0 = S.count("0")
    c1 = S.count("1")
    # 0と1の数が少ない方を答えとする
    print(min(c0, c1))

main()

=======
Suggestion 8

def main():
    S = input()
    N = len(S)
    # 前から塗っていく場合
    cnt1 = 0
    for i in range(N):
        if (i % 2 == 0 and S[i] == '1') or (i % 2 == 1 and S[i] == '0'):
            cnt1 += 1
    # 後ろから塗っていく場合
    cnt2 = 0
    for i in range(N):
        if (i % 2 == 0 and S[N - 1 - i] == '1') or (i % 2 == 1 and S[N - 1 - i] == '0'):
            cnt2 += 1
    print(min(cnt1, cnt2))

=======
Suggestion 9

def main():
    S = input()
    N = len(S)
    # 0を黒, 1を白とする
    # 0を黒にしたときの最小塗り替え回数
    count0 = 0
    # 1を白にしたときの最小塗り替え回数
    count1 = 0
    # 0を黒にしたときの前のタイルの色
    prev0 = 0
    # 1を白にしたときの前のタイルの色
    prev1 = 1
    for i in range(N):
        if S[i] == '0':
            if prev0 == 0:
                count0 += 1
                prev0 = 1
            else:
                prev0 = 0
        else:
            if prev0 == 1:
                count0 += 1
                prev0 = 0
            else:
                prev0 = 1
        if S[i] == '1':
            if prev1 == 0:
                count1 += 1
                prev1 = 1
            else:
                prev1 = 0
        else:
            if prev1 == 1:
                count1 += 1
                prev1 = 0
            else:
                prev1 = 1
    print(min(count0, count1))
