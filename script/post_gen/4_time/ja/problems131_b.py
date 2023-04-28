Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, L = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        ans += L + i - 1
    if L > 0:
        ans -= L + N - 1
    elif L+N-1 < 0:
        ans -= L
    print(ans)

=======
Suggestion 2

def main():
    N, L = map(int, input().split())
    ans = 0
    if L >= 0:
        ans = (L + N - 1) * (L + N) // 2 - L
    elif L + N - 1 < 0:
        ans = (L + N - 1) * (L + N) // 2 - L
    else:
        ans = (L + N - 1) * (L + N) // 2
    print(ans)

=======
Suggestion 3

def solve():
    N, L = map(int, input().split())
    sum = 0
    min = 1000
    for i in range(N):
        sum += L + i
        if min > abs(L + i):
            min = abs(L + i)
    print(sum - min)

=======
Suggestion 4

def main():
    n, l = map(int, input().split())
    apple = []
    for i in range(1, n+1):
        apple.append(l+i-1)
    print(sum(apple)-min(apple, key=abs))

=======
Suggestion 5

def solve():
    N, L = map(int, input().split())
    print(sum(range(L+1, L+N)) - min(range(L+1, L+N), key=abs))

=======
Suggestion 6

def main():
    n,l = map(int, input().split())
    ans = 0
    if l >= 0:
        ans = sum(range(l+1, l+n))
    elif l+n-1 < 0:
        ans = sum(range(l, l+n-1))
    else:
        ans = sum(range(l, l+n))
    print(ans)

=======
Suggestion 7

def main():
    n, l = map(int, input().split())
    sum = 0
    min =

=======
Suggestion 8

def apple_pie(n, l):
    taste = []
    for i in range(n):
        taste.append(l+i)
    taste.sort()
    return sum(taste[1:])

=======
Suggestion 9

def main():
    N,L = map(int,input().split())
    total = 0
    min_

=======
Suggestion 10

def main():
    # 標準入力からNとLを取得する
    N, L = map(int, input().split())

    # リンゴの味のリスト
    apples = []
    # リンゴの味を計算する
    for i in range(N):
        apples.append(L + i)

    # リンゴの味の総和
    total = sum(apples)

    # リンゴの味の絶対値の最小値
    min_abs = 1000000
    # リンゴの味の総和からリンゴの味を引いた絶対値の最小値を計算する
    for i in range(N):
        abs = total - apples[i]
        if abs < 0:
            abs = abs * -1
        if abs < min_abs:
            min_abs = abs

    # 答えを出力する
    print(min_abs)
