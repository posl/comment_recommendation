Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    
    #print(n)
    #print(s)
    #print(w)
    
    #子供の数をカウント
    count = 0
    for i in range(n):
        if s[i] == '0':
            count += 1
    
    #print(count)
    
    #重さのリストを作成
    weight = []
    for i in range(n):
        if s[i] == '0':
            weight.append(w[i])
    
    #print(weight)
    
    #重さのリストをソート
    weight.sort()
    
    #print(weight)
    
    #重さのリストの重複を削除
    weight = list(set(weight))
    
    #print(weight)
    
    #重さのリストの重複を削除した結果の長さを取得
    weight_len = len(weight)
    
    #print(weight_len)
    
    #重さのリストの重複を削除した結果の長さが1の場合
    if weight_len == 1:
        #子供の数を出力
        print(count)
        #終了
        exit()
    
    #重さのリストの重複を削除した結果の長さが2の場合
    if weight_len == 2:
        #子供の数を出力
        print(count)
        #終了
        exit()
    
    #重さのリストの重複を削除した結果の長さが3以上の場合
    if weight_len >= 3:
        #子供の数を出力
        print(count)
        #終了
        exit()

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    W = list(map(int,input().split()))
    w = []
    for i in range(N):
        if S[i] == "0":
            w.append(W[i])
    w.sort()
    if len(w) == 0:
        print(0)
        exit()
    if len(w) == 1:
        print(1)
        exit()
    if len(w) == 2:
        print(2)
        exit()
    if len(w) == 3:
        print(3)
        exit()
    if len(w) == 4:
        print(4)
        exit()
    if len(w) == 5:
        print(4)
        exit()
    if len(w) == 6:
        print(5)
        exit()
    if len(w) == 7:
        print(5)
        exit()
    if len(w) == 8:
        print(5)
        exit()
    if len(w) == 9:
        print(6)
        exit()
    if len(w) == 10:
        print(6)
        exit()
    if len(w) == 11:
        print(6)
        exit()
    if len(w) == 12:
        print(7)
        exit()
    if len(w) == 13:
        print(7)
        exit()
    if len(w) == 14:
        print(7)
        exit()
    if len(w) == 15:
        print(7)
        exit()
    if len(w) == 16:
        print(8)
        exit()
    if len(w) == 17:
        print(8)
        exit()
    if len(w) == 18:
        print(8)
        exit()
    if len(w) == 19:
        print(8)
        exit()
    if len(w) == 20:
        print(9)
        exit()
    if len(w) == 21:
        print(9)
        exit()
    if len(w) == 22:
        print(9)
        exit()
    if len(w) == 23:
        print(9)
        exit()
    if len(w) == 24:
        print(10)
        exit()
    if len(w) == 25:
        print(10)
        exit()
    if len(w)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    child = [0] * N
    adult = [0] * N
    for i in range(N):
        if S[i] == '0':
            child[i] = W[i]
        else:
            adult[i] = W[i]
    child = sorted(child, reverse=True)
    adult = sorted(adult, reverse=True)
    for i in range(1, N):
        child[i] += child[i-1]
        adult[i] += adult[i-1]
    ans = 0
    for i in range(N):
        if i == 0:
            if child[i] > adult[i]:
                ans += 1
        else:
            if child[i] + adult[i-1] > adult[i] + child[i-1]:
                ans += 1
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if S[i] == '1':
            cnt += 1
    if cnt == 0 or cnt == N:
        print(N)
        return
    #累積和を作る
    cumsum = [0] * (N + 1)
    for i in range(N):
        cumsum[i + 1] = cumsum[i] + W[i]
    ans = 0
    for i in range(1, N):
        if S[i] == '1':
            continue
        #i番目の人を大人とする
        left = cumsum[i] / i
        #i番目の人を子供とする
        right = (cumsum[N] - cumsum[i]) / (N - i)
        if left < right:
            ans = max(ans, i)
    print(ans + cnt)

solve()

=======
Suggestion 5

def isChild(w,x):
    if w < x:
        return True
    else:
        return False

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))

    w1 = [0] * n
    w2 = [0] * n
    for i in range(n):
        if s[i] == '0':
            w1[i] = w[i]
        else:
            w2[i] = w[i]

    for i in range(1, n):
        w1[i] += w1[i-1]
        w2[i] += w2[i-1]

    ans = 0
    for i in range(n):
        if s[i] == '0':
            ans = max(ans, w1[i] + w2[n-1] - w2[i])
        else:
            ans = max(ans, w2[i] + w1[n-1] - w1[i])

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    W = list(map(int,input().split()))
    ans = 0
    for i in range(1,N):
        if S[i] == '1':
            ans += 1
    ans_ = ans
    if S[0] == '0':
        ans_ += 1
    else:
        ans_ -= 1
    ans__ = ans_
    for i in range(1,N):
        if S[i] == '0':
            ans_ += 1
        else:
            ans_ -= 1
        ans__ = max(ans__,ans_)
    ans = 0
    for i in range(1,N):
        if S[i] == '1':
            ans += 1
    ans_ = ans
    if S[0] == '1':
        ans_ += 1
    else:
        ans_ -= 1
    ans__ = ans_
    for i in range(1,N):
        if S[i] == '1':
            ans_ += 1
        else:
            ans_ -= 1
        ans__ = max(ans__,ans_)
    print(ans__)

=======
Suggestion 8

def main():
    # 1行目の入力を取得
    n = int(input())
    # 2行目の入力を取得
    s = input()
    # 3行目の入力を取得
    w = list(map(int, input().split()))
    # f(x)を求める
    def f(x):
        cnt = 0
        for i in range(n):
            if s[i] == '0':
                if w[i] < x:
                    cnt += 1
            else:
                if w[i] >= x:
                    cnt += 1
        return cnt
    # Xを動かす範囲を定義
    left = 0
    right = 10 ** 9 + 1
    # 二分探索
    while right - left > 1:
        mid = (left + right) // 2
        if f(mid) == n:
            left = mid
        else:
            right = mid
    # 答えを出力
    print(left)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if S[i] == '0' and S[i - 1] == '1':
            ans += 1
    if ans == N - 1:
        print(N)
        exit()
    if ans == 0:
        print(0)
        exit()
    ans += 1
    for i in range(N):
        if S[i] == '1':
            W[i] = 0
    L = []
    for i in range(N):
        if S[i] == '0':
            L.append(W[i])
    L.sort()
    ans += L[-1]
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    l = 0
    r = 10**9+1
    while r-l > 1:
        m = (r+l)//2
        flag = True
        for i in range(n):
            if s[i] == '0' and w[i] >= m:
                flag = False
                break
        if flag:
            l = m
        else:
            r = m
    print(l)
