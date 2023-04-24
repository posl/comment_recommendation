Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # N = 5
    # S = '10101'
    # W = [60, 45, 30, 40, 80]
    # N = 3
    # S = '000'
    # W = [1, 2, 3]
    # N = 5
    # S = '10101'
    # W = [60, 50, 50, 50, 60]

    # 体重の昇順にソート
    W = sorted(W)
    # print(W)

    # 体重の昇順にソートしたときの、各体重の人数を求める
    # 体重が同じ人がいる場合は、同じ体重の人数を加算する
    num = 1
    w = []
    for i in range(N - 1):
        if W[i] == W[i + 1]:
            num += 1
        else:
            w.append(num)
            num = 1
    w.append(num)
    # print(w)

    # 体重の昇順にソートしたときの、各体重の人数の累積和を求める
    # 体重が同じ人がいる場合は、同じ体重の人数を加算する
    w_sum = [w[0]]
    for i in range(1, len(w)):
        w_sum.append(w_sum[i - 1] + w[i])
    # print(w_sum)

    # 体重の昇順にソートしたときの、各体重の人数の累積和のリストを逆順にする
    w_sum = w_sum[::-1]
    # print(w_sum)

    # 体重の降順にソート
    W = sorted(W, reverse=True)
    # print(W)

    # 判定を正しく行える人数の最大値を求める
    # Sのi文字目が0の場合は、W[i]

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W1 = []
    W2 = []
    for i in range(N):
        if S[i] == "0":
            W1.append(W[i])
        else:
            W2.append(W[i])
    W1.sort()
    W2.sort()
    ans = 0
    for i in range(N):
        if S[i] == "0":
            idx = bisect_left(W2, W[i])
            ans = max(ans, idx + N - i - 1)
        else:
            idx = bisect_right(W1, W[i])
            ans = max(ans, i - idx + 1)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if S[j] == "0" and W[j] < W[i]:
                cnt += 1
            if S[j] == "1" and W[j] >= W[i]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    S = S[::-1]
    W = W[::-1]
    ans = 0
    for i in range(N):
        if S[i] == '0':
            if W[i] < W[ans]:
                ans = i
        else:
            if W[i] > W[ans]:
                ans = i
    print(ans+1)

=======
Suggestion 5

def main():
    # 入力
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # 処理
    ans = 0
    for i in range(1, N):
        if S[i] != S[i-1]:
            ans += 1
    # 出力
    print(ans+1)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))

    # 体重の昇順に並び替え
    W_sort = sorted(W)
    # 体重の昇順に並び替えたときのインデックス
    W_sort_index = sorted(range(N), key=lambda x: W[x])
    # 体重の昇順に並び替えたときのインデックスの逆順
    W_sort_index_reverse = sorted(range(N), key=lambda x: W[x], reverse=True)

    # 体重の昇順に並び替えたときの、体重が i 以上の人数
    W_sort_cnt = [0] * (N + 1)
    for i in range(N):
        W_sort_cnt[i + 1] = W_sort_cnt[i] + (S[W_sort_index[i]] == '1')

    # 体重の降順に並び替えたときの、体重が i 未満の人数
    W_sort_reverse_cnt = [0] * (N + 1)
    for i in range(N):
        W_sort_reverse_cnt[i + 1] = W_sort_reverse_cnt[i] + (S[W_sort_index_reverse[i]] == '0')

    ans = 0
    for i in range(N):
        ans = max(ans, W_sort_cnt[i] + W_sort_reverse_cnt[N - i])

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    #print(N, S, W)

    # 体重の昇順に並び替える
    W.sort()

    # Xの候補を列挙する
    X = []
    for i in range(N-1):
        if W[i] != W[i+1]:
            X.append((W[i] + W[i+1]) / 2)

    #print(X)

    # Xの候補の中で最大値を求める
    ans = 0
    for x in X:
        cnt = 0
        for i in range(N):
            if W[i] < x and S[i] == '0':
                cnt += 1
            elif W[i] >= x and S[i] == '1':
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    #print(N,S,W)
    #print(S[0])
    #print(W[0])

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    w = [int(i) for i in input().split()]
    #print(n,s,w)
    
    #初期化
    t = [0 for i in range(n)]
    for i in range(n):
        t[i] = 1 if s[i] == "1" else 0
    #print(t)
    
    #初期化
    ans = 0
    #Xを動かしていく
    for x in range(1,1000000001):
        #初期化
        cnt = 0
        #Xを動かしていく
        for i in range(n):
            if w[i] >= x and t[i] == 1:
                cnt += 1
            elif w[i] < x and t[i] == 0:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    #print(n, s, w)
    #print(len(s), len(w), n)

    # 体重の小さい順にソート
    # 体重が同じ人は、sの値が小さい順にソート
    # 体重が同じ人は、sの値が小さい順にソート
    w_s = sorted(zip(w, s), key=lambda x: (x[0], x[1]))
    #print(w_s)

    # 体重の小さい順にソートしたリスト
    w_sort = [x[0] for x in w_s]
    #print(w_sort)

    # sの値が小さい順にソートしたリスト
    s_sort = [x[1] for x in w_s]
    #print(s_sort)

    # 体重の小さい順にソートしたリストの中で、sの値が0の人の数
    #print(s_sort.count('0'))

    # 体重の小さい順にソートしたリストの中で、sの値が0の人の数の最大値
    #print(max(s_sort.count('0'), s_sort.count('1')))

    # 体重の小さい順にソートしたリストの中で、sの値が0の人の数の最大値を出力
    print(max(s_sort.count('0'), s_sort.count('1')))
