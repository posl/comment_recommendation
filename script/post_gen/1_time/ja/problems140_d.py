Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == 'L':
            ans += 1
        else:
            break
    for i in range(N-1, -1, -1):
        if S[i] == 'R':
            ans += 1
        else:
            break
    ans = min(ans + 2*K, N)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == 'L':
            cnt = 0
            for j in range(i, -1, -1):
                if S[j] == 'L':
                    cnt += 1
                else:
                    break
            ans = max(ans, cnt)
        else:
            cnt = 0
            for j in range(i, N):
                if S[j] == 'R':
                    cnt += 1
                else:
                    break
            ans = max(ans, cnt)
    print(min(ans + 2 * K, N))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        elif S[i] != S[i - 1]:
            ans += 1
    if ans % 2 == 0:
        ans -= 1
    print(min(ans + 2 * K, N))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "R":
            if i == 0:
                ans += 1
            else:
                if S[i - 1] == "L":
                    ans += 1
    for i in range(N - 1, -1, -1):
        if S[i] == "L":
            if i == N - 1:
                ans += 1
            else:
                if S[i + 1] == "R":
                    ans += 1
    ans = min(ans + 2 * K, N)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "L":
            r = i
            for j in range(i-1, -1, -1):
                if S[j] == "R":
                    l = j
                    break
            else:
                l = -1
        else:
            l = i
            for j in range(i+1, N):
                if S[j] == "L":
                    r = j
                    break
            else:
                r = N
        ans = max(ans, r - l - 1)
    print(min(ans + 2*K, N))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = input()
    S = S + S
    ans = 0
    for i in range(N):
        if S[i] == "R":
            ans += 1
            if S[i+1] == "L":
                ans += 1
    if ans == N:
        ans = N - 1
    ans = min(ans + 2 * K, N)
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = input()
    #K回の操作で幸福になれる人数の最大値を求める
    #K回の操作で幸福になれる人数の最大値は、
    #K回の操作で幸福になれる人数の最大値のうち、
    #最小のものと等しい
    #K回の操作で幸福になれる人数の最大値は、
    #K回の操作で幸福になれる人数の最大値のうち、
    #最小のものと等しい
    #K回の操作で幸福になれる人数の最大値は、
    #K回の操作で幸福になれる人数の最大値のうち、
    #最小のものと等しい
    #K回の操作で幸福になれる人数の最大値は、
    #K回の操作で幸福になれる人数の最大値のうち、
    #最小のものと等しい
    #K回の操作で幸福になれる人数の最大値は、
    #K回の操作で幸福になれる人数の最大値のうち、
    #最小のものと等しい
    #K回の操作で幸福になれる人数の最大値は、
    #K回の操作で幸福になれる人数の最大値のうち、
    #最小のものと等しい
    #K回の操作で幸福になれる人数の最大値は、
    #K回の操作で幸福になれる人数の最大値のうち、
    #最小のものと等しい
    #K回の操作

=======
Suggestion 8

def main():
    # 入力
    N, K = map(int, input().split())
    S = input()
    # 連続するLの数を保持する配列
    L = []
    # 連続するRの数を保持する配列
    R = []
    # 連続するLの数を数える
    count = 0
    for i in range(N):
        if S[i] == "L":
            count += 1
        else:
            L.append(count)
            count = 0
    L.append(count)
    # 連続するRの数を数える
    count = 0
    for i in range(N):
        if S[N-i-1] == "R":
            count += 1
        else:
            R.append(count)
            count = 0
    R.append(count)
    # Rの数が多い順にソート
    R.sort(reverse=True)
    # 操作
    ans = 0
    for i in range(min(K, len(R))):
        ans += R[i]
    # 連続するLの数が偶数の場合、幸福な人数を増やす
    for i in range(len(L)):
        if L[i] % 2 == 0:
            ans += L[i]
    # 出力
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    #Lの連続する個数を記録するリスト
    L_list = []
    #Rの連続する個数を記録するリスト
    R_list = []
    #Lの連続する個数を記録する変数
    L = 0
    #Rの連続する個数を記録する変数
    R = 0
    #Sの最初がLの場合
    if S[0] == "L":
        #Lの連続する個数を記録するリストに0を追加
        L_list.append(0)
    #Sの最初がRの場合
    else:
        #Rの連続する個数を記録するリストに0を追加
        R_list.append(0)
    #Sの各文字について
    for i in range(N):
        #Sのi文字目がLの場合
        if S[i] == "L":
            #Lの連続する個数を記録する変数に1を加える
            L += 1
            #Rの連続する個数を記録する変数が0でない場合
            if R != 0:
                #Rの連続する個数を記録するリストにRの連続する個数を記録する変数を追加
                R_list.append(R)
                #Rの連続する個数を記録する変数を0にする
                R = 0
        #Sのi文字目がRの場合
        else:
            #Rの連続する個数を記録する変数に1を加える
            R += 1
            #Lの連続する個数を記録する変数が0でない場合
            if L != 0:
                #Lの連続する

=======
Suggestion 10

def main():
    #入力
    N, K = map(int, input().split())
    S = input()

    #初期値
    ans = 0
    #0 から N-1 までの各 i について、
    #i から左に向かって連続する L の数を Lcnt[i] とする。
    Lcnt = [0] * N
    #i から右に向かって連続する R の数を Rcnt[i] とする。
    Rcnt = [0] * N

    #Lcnt, Rcnt を求める
    for i in range(N):
        if S[i] == "L":
            if i == 0:
                Lcnt[i] = 1
            else:
                Lcnt[i] = Lcnt[i-1] + 1
        else:
            Lcnt[i] = 0

    for i in range(N-1, -1, -1):
        if S[i] == "R":
            if i == N-1:
                Rcnt[i] = 1
            else:
                Rcnt[i] = Rcnt[i+1] + 1
        else:
            Rcnt[i] = 0

    #0 から N-1 までの各 i について、
    #i から左に向かって連続する L の数が K より大きいならば、
    #Lcnt[i] + Rcnt[i] が答えである。
    #そうでないならば、Lcnt[i] + Rcnt[i] - 1 が答えである。
    for i in range(N):
        if Lcnt[i] > K:
            ans = max(ans, Lcnt[i] + Rcnt[i])
        else:
            ans = max(ans, Lcnt[i] + Rcnt[i] - 1)

    #出力
    print(ans)
