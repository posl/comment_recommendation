Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    if a * n < b:
        print(a * n)
    else:
        print(b)

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    print(min(n * a, b))

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    print(min(A*N, B))

=======
Suggestion 4

def main():
    # 標準入力から N, A, B を取得する
    N, A, B = map(int, input().split())

    # N 人の交通費の合計の最小値を出力する
    print(min(A*N, B))

=======
Suggestion 5

def calc_min_cost(n, a, b):
    return min(n * a, b)
