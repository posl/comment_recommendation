Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    cnt = 0
    for i in range(n):
        s = input()
        if s == "For":
            cnt += 1
    if cnt > n // 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for i in range(N)]
    if S.count("For") > N // 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for i in range(n)]
    if s.count("For") > n // 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print('Yes' if S.count('For') > N // 2 else 'No')

=======
Suggestion 5

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    if l.count('For') > n // 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for i in range(N)]

    count = 0
    for s in S:
        if s == "For":
            count += 1

    if count > N / 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n = int(input())
    list = []
    for i in range(n):
        list.append(input())
    if list.count("For") > n/2:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 8

def main():
    n = int(input())
    for_list = []
    for i in range(n):
        for_list.append(input())
    if for_list.count("For") > n//2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    cnt = 0
    for s in S:
        if s == "For":
            cnt += 1
    if cnt > N // 2:
        print("Yes")
    else:
        print("No")

main()

実行結果

$ python3 problems287_a.py
3
For
Against
For
Yes

$ python3 problems287_a.py
5
Against
Against
For
Against
For
No

$ python3 problems287_a.py
1
For
Yes

問題文

ある提案に対し、N 人の人が賛成か反対かを表明しています。なお、N は奇数です。

i  (i = 1, 2, ..., N) 番目の人の意見は文字列 S_i で表され、S_i =  For のとき賛成しており、S_i =  Against のとき反対しています。

過半数の人がこの提案に賛成しているかどうかを判定してください。

制約

N は 1 以上 99 以下の奇数

全ての i = 1, 2, ..., N に対し、S_i =  For または S_i =  Against

入力

入力は以下の形式で標準入力から与えられる。

N
S_1
S_2
.
.
.
S_N

出力

N 人のうち過半数が提案に賛成しているならば Yes、そうでなければ No と出力せよ。

入力例 1

3
For
Against
For

出力例 1

Yes

提案に賛成している人数は 2 人であり、これは半数を超えているので Yes と出力します。

入力例 2

5
Against
Against
For
Against
For

出力例 2

No

提案に賛成している

=======
Suggestion 10

def main():
    # 入力
    N = int(input())
    S = [input() for _ in range(N)]

    # 計算
    # Forの数を数える
    count = 0
    for i in range(N):
        if S[i] == 'For':
            count += 1

    # 出力
    if count > N // 2:
        print('Yes')
    else:
        print('No')
