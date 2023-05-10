Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 標準入力を取得
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    # 一番人気のジェットコースターに乗ることができる人の数を求める
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1

    # 結果を出力
    print(count)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    h_list = list(map(int, input().split()))
    count = 0
    for i in h_list:
        if i >= K:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    # 1行目の入力を受け取る
    # 入力値は文字列なので、split()でスペース区切りにし、map()でint型に変換してlist化する
    n, k = map(int, input().split())
    # 2行目の入力を受け取る
    h = list(map(int, input().split()))
    #print(n, k, h)

    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1

    print(count)
    return

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in h:
        if i >= k:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if k <= h[i]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if h[i] >= k:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if k <= h[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    h = list(map(int,input().split()))
    cnt = 0
    for i in range(N):
        if h[i] >= K:
            cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if h[i] >= K:
            ans += 1
    print(ans)
