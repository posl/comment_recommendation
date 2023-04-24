Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            S += "B"
            N //= 2
        else:
            S += "A"
            N -= 1
    print(S[::-1])

=======
Suggestion 2

def main():
    N = int(input())
    S = ''
    while N > 0:
        if N % 2 == 0:
            S += 'B'
            N //= 2
        else:
            S += 'A'
            N -= 1
    print(S[::-1])

=======
Suggestion 3

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            N //= 2
            S += "B"
        else:
            N -= 1
            S += "A"
    print(S[::-1])

=======
Suggestion 4

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            S = "B" + S
            N //= 2
        else:
            S = "A" + S
            N -= 1
    print(S)

=======
Suggestion 5

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 1:
            S = "A" + S
            N -= 1
        else:
            S = "B" + S
            N //= 2
    print(S)

=======
Suggestion 6

def main():
    N = int(input())
    ans = ''
    while N > 0:
        if N % 2 == 0:
            ans += 'B'
            N //= 2
        else:
            ans += 'A'
            N -= 1
    print(ans[::-1])

=======
Suggestion 7

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            N //= 2
            S = "B" + S
        else:
            N -= 1
            S = "A" + S
    print(S)

=======
Suggestion 8

def main():
    N = int(input())
    ans = []
    while N > 0:
        if N % 2 == 0:
            ans.append('B')
            N //= 2
        else:
            ans.append('A')
            N -= 1
    ans.reverse()
    print(''.join(ans))

=======
Suggestion 9

def main():
    N = int(input())
    # 2進数に変換
    N = bin(N)[2:]
    # 2進数の桁数
    N_len = len(N)
    # 答え
    ans = ''
    # 2進数の最下位桁から順に処理
    for i in range(N_len):
        # 下からi桁目の数字
        d = N[N_len-i-1]
        # 1の場合
        if d == '1':
            # 2のi乗
            ans += 'A'*(i+1)
            # 2のi乗-1
            ans += 'B'
        # 0の場合
        else:
            # 2のi乗-1
            ans += 'A'
    # 末尾のBを削除
    ans = ans[:-1]
    print(ans)
