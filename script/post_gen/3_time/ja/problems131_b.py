Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, L = map(int, input().split())
    apple_pie = [L + i - 1 for i in range(1, N + 1)]
    print(sum(apple_pie) - min(apple_pie, key=abs))

=======
Suggestion 2

def main():
    N, L = map(int, input().split())
    if L <= 0 and L+N-1 >= 0:
        print(sum(range(L, L+N)))
    elif L <= 0 and L+N-1 < 0:
        print(sum(range(L, L+N-1)))
    else:
        print(sum(range(L+1, L+N)))

=======
Suggestion 3

def main():
    N, L = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        sum += L+i-1
    if L >= 0:
        print(sum - L)
    elif L+N-1 <= 0:
        print(sum - (L+N-1))
    else:
        print(sum)

=======
Suggestion 4

def main():
    N, L = map(int, input().split())
    # N, L = 30, -50
    # N, L = 3, -1
    # N, L = 5, 2

    # 1 2 3 4 5
    # 2 3 4 5 6
    # 3 4 5 6 7
    # 4 5 6 7 8
    # 5 6 7 8 9
    # 6 7 8 9 10
    # 7 8 9 10 11
    # 8 9 10 11 12
    # 9 10 11 12 13
    # 10 11 12 13 14
    # 11 12 13 14 15
    # 12 13 14 15 16
    # 13 14 15 16 17
    # 14 15 16 17 18
    # 15 16 17 18 19
    # 16 17 18 19 20
    # 17 18 19 20 21
    # 18 19 20 21 22
    # 19 20 21 22 23
    # 20 21 22 23 24
    # 21 22 23 24 25
    # 22 23 24 25 26
    # 23 24 25 26 27
    # 24 25 26 27 28
    # 25 26 27 28 29
    # 26 27 28 29 30
    # 27 28 29 30 31
    # 28 29 30 31 32
    # 29 30 31 32 33
    # 30 31 32 33 34

    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29

=======
Suggestion 5

def main():
    N, L = map(int, input().split())
    print(N*(2*L+N-1)//2-L)

=======
Suggestion 6

def main():
    N, L = map(int, input().split())
    apples = [L+i-1 for i in range(1, N+1)]
    eaten = apples.pop(apples.index(min(apples, key=abs)))
    print(sum(apples))

=======
Suggestion 7

def main():
    N, L = map(int, input().split())
    # 全てのリンゴの味を求める
    apple_taste = [L + i - 1 for i in range(1, N + 1)]
    # 一番味が悪いリンゴを食べる
    if L <= 0 and 0 <= L + N - 1:
        print(sum(apple_taste))
    # 一番味が悪いリンゴを食べる
    elif L < 0:
        print(sum(apple_taste) - apple_taste[0])
    # 一番味が悪いリンゴを食べる
    elif L + N - 1 < 0:
        print(sum(apple_taste) - apple_taste[-1])

=======
Suggestion 8

def main():
    N, L = map(int, input().split())
    # L から L+N-1 までの和を求める
    total = sum([L+i-1 for i in range(1, N+1)])
    # 食べるリンゴを決める
    if L >= 0:
        # L が 0 以上の場合、最小値は L である
        eat = L
    elif L+N-1 <= 0:
        # L+N-1 が 0 以下の場合、最小値は L+N-1 である
        eat = L+N-1
    else:
        # L 以上 L+N-1 以下の場合、最小値は 0 である
        eat = 0
    # 食べるリンゴを除いた和を求める
    print(total - eat)

=======
Suggestion 9

def main():
    # 1行目の入力
    n, l = map(int, input().split())
    # リストの初期化
    apple = []
    # リストの作成
    for i in range(n):
        apple.append(l+i)
    # 最適なリンゴを食べる
    apple.remove(min(apple, key=lambda x: abs(x)))
    # リンゴの味の合計を求める
    print(sum(apple))

=======
Suggestion 10

def main():
    N, L = map(int, input().split())
    # 1個食べるリンゴを選ぶ
    # 1個食べたら、食べていないN-1個のリンゴを材料としてできるアップルパイの味を求める
    # 1個食べるリンゴを選ぶとき、食べていないN-1個のリンゴを材料としてできるアップルパイの味の差の絶対値ができるだけ小さくなるように選ぶ
    # 1個食べるリンゴを選ぶとき、食べていないN-1個のリンゴを材料としてできるアップルパイの味の差の絶対値ができるだけ小さくなるように選ぶということは、
    # 1個食べるリンゴを選ぶとき、食べていないN-1個のリンゴを材料としてできるアップルパイの味の差ができるだけ小さくなるように選ぶということ
    # 1個食べるリンゴを選ぶとき、食べていないN-1個のリンゴを材料としてできるアップルパイの味の差ができるだけ小さくなるように選ぶということは、
    # 1個食べるリンゴを選ぶとき、食べていないN-1個のリンゴを材料としてできるアップルパイの
