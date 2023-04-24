Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(1, N):
        if H[i-1] >= H[i]:
            cnt += 1
            if cnt > ans:
                ans = cnt
        else:
            cnt = 0
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    max_cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            cnt = 0
        max_cnt = max(max_cnt, cnt)
    print(max_cnt)

main()

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(1, N):
        if H[i] <= H[i-1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    print(max(ans, cnt))

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    tmp = 0
    for i in range(1, N):
        if H[i-1] >= H[i]:
            tmp += 1
        else:
            tmp = 0
        cnt = max(cnt, tmp)
    print(cnt)

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    H = list(map(int, input().split()))
    #処理
    count = 0
    for i in range(1, N):
        if H[i - 1] >= H[i]:
            count += 1
        else:
            count = 0
    #出力
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))

    # 最大移動回数
    max_move = 0
    # 今までの移動回数
    move = 0

    # 最後のマスまで移動
    for i in range(N-1):
        # 次のマスの高さが現在のマスの高さ以下のとき
        if H[i] >= H[i+1]:
            # 今までの移動回数をインクリメント
            move += 1
        # 次のマスの高さが現在のマスの高さより高いとき
        else:
            # 今までの移動回数をリセット
            move = 0

        # 最大移動回数を更新
        if move > max_move:
            max_move = move

    # 最大移動回数を出力
    print(max_move)
