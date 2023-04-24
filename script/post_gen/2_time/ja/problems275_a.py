Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(H.index(max(H)) + 1)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(a.index(max(a)) + 1)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int,input().split()))
    m = 0
    ans = 0
    for i in range(N):
        if m < H[i]:
            m = H[i]
            ans = i+1
    print(ans)

=======
Suggestion 4

def main():
    # 標準入力から整数を受け取る
    N = int(input())
    # 標準入力から整数のリストを受け取る
    H = list(map(int, input().split()))
    # 最も高い橋の高さを求める
    H_max = max(H)
    # 最も高い橋の何番目にあるかを求める
    H_max_idx = H.index(H_max) + 1
    # 結果を出力する
    print(H_max_idx)

=======
Suggestion 5

def main():
    #入力
    N = int(input())
    H = list(map(int, input().split()))
    #最大値のインデックスを取得
    ans = H.index(max(H))
    #出力
    print(ans+1)

=======
Suggestion 6

def main():
    #入力
    N = int(input())
    H = list(map(int,input().split()))

    #処理
    max = 0
    for i in range(0,N):
        if H[i] > max:
            max = H[i]
            ans = i + 1

    #出力
    print(ans)
