Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K, X = map(int, input().split())
    for i in range(X - K + 1, X + K):
        print(i, end=' ')

=======
Suggestion 2

def main():
    K, X = map(int, input().split())
    for i in range(X-K+1, X+K):
        print(i, end=" ")

=======
Suggestion 3

def main():
    k, x = map(int, input().split())
    for i in range(x-k+1, x+k):
        print(i, end=' ')

=======
Suggestion 4

def main():
    K, X = map(int, input().split())
    print(*range(X - K + 1, X + K))

=======
Suggestion 5

def main():
    k, x = map(int, input().split())
    print(' '.join(map(str, [x - i for i in range(k - 1, -1, -1)] + [x + i for i in range(1, k)])))

=======
Suggestion 6

def main():
    K, X = map(int, input().split())
    print(*[i for i in range(X-K+1, X+K)], sep=' ')

=======
Suggestion 7

def get_black_stone(K, X):
    # 黒で塗られている石が置かれている可能性のある座標をすべて、小さい順に出力してください。
    # ここに処理を書き加えてください
    for i in range(-K+1, K):
        print(X+i, end = " ")

=======
Suggestion 8

def main():
    K, X = map(int, input().split())
    for i in range(K):
        print(X - K + i + 1, end=' ')
    print()
