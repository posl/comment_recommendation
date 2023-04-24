Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    K = int(input())
    N = len(S)
    ans = 0
    cnt = 0
    for i in range(N):
        if S[i] == 'X':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    ans += K
    ans = min(ans, N)
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    K = int(input())
    N = len(S)
    cnt = 0
    ans = 0
    for i in range(N):
        if S[i] == 'X':
            cnt += 1
        else:
            if cnt >= K:
                cnt -= K
                ans += K
                K = 0
            else:
                K -= cnt
                ans += cnt
                cnt = 0
    print(ans + min(cnt, K))

=======
Suggestion 3

def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    i = 0
    while i < n:
        if s[i] == 'X':
            i += 1
            continue
        j = i
        while j < n and s[j] == '.':
            j += 1
        ans = max(ans, j - i)
        i = j
    ans = min(ans + k * 2, n)
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    K = int(input())
    N = len(S)
    if N == 1:
        print(1)
        return
    if S[0] == '.':
        S = 'X' + S
        N += 1
    if S[-1] == '.':
        S = S + 'X'
        N += 1
    S = S.replace('.', 'X')
    #print(S)
    max = 0
    cnt = 0
    for i in range(1, N):
        if S[i] == 'X':
            cnt += 1
        else:
            if cnt > max:
                max = cnt
            cnt = 0
    if cnt > max:
        max = cnt
    #print(max)
    if max > K:
        max = K
    print(max + 1)

=======
Suggestion 5

def main():
    S = input()
    K = int(input())
    N = len(S)
    ans = 0
    for i in range(N):
        for j in range(i, N):
            ans = max(ans, j - i + 1 - S[i:j+1].count("X"))
    print(min(ans + K, N))

=======
Suggestion 6

def main():
    S = input()
    K = int(input())
    N = len(S)
    ans = 0
    # 連続する X の数を数える
    cnt = 0
    for i in range(N):
        if S[i] == 'X':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    # X の数が K 以上の場合は、X を K 個連続させる
    if ans >= K:
        ans = K
    # X の数が K 未満の場合は、X を ans 個連続させる
    else:
        ans += (K - ans) // 2 * 2
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    K = int(input())
    S = S.replace(".", "X")
    if K == 0:
        print(S.count("X"))
        return
    if K >= len(S):
        print(len(S))
        return
    for i in range(len(S)):
        if S[i] == "X":
            S = S[:i] + "." + S[i + 1:]
            break
    for i in range(len(S) - 1, -1, -1):
        if S[i] == "X":
            S = S[:i] + "." + S[i + 1:]
            break
    print(S.count("X") + 1)

=======
Suggestion 8

def main():
    s = input()
    k = int(input())
    #print(s)
    #print(k)
    s = s.replace(".","X")
    #print(s)
    s = s.replace("X","X.")
    #print(s)
    s_list = s.split(".")
    #print(s_list)
    s_list = [i for i in s_list if i != ""]
    #print(s_list)
    if len(s_list) == 1:
        print(len(s_list[0]))
    else:
        if k >= len(s_list)-1:
            print(len(s))
        else:
            s_list.sort(key=lambda x:len(x))
            #print(s_list)
            l = len(s_list[0])
            for i in range(k):
                l += len(s_list[i+1])
            print(l)

=======
Suggestion 9

def main():
    S = input()
    K = int(input())
    N = len(S)
    #Xの連続個数を記録する配列
    X = []
    #Xの連続個数を記録する
    for i in range(N):
        if i == 0:
            X.append(1)
        else:
            if S[i] == S[i-1]:
                X[-1] += 1
            else:
                X.append(1)
    #Xの連続個数が奇数の時、その数を2で割る
    for i in range(len(X)):
        if X[i] % 2 == 1:
            X[i] //= 2
    #Xの連続個数を累積和にする
    for i in range(1,len(X)):
        X[i] += X[i-1]
    #Xの連続個数が奇数の時、その数を2で割る
    for i in range(len(X)):
        if X[i] % 2 == 1:
            X[i] //= 2
    #Xの連続個数の累積和の最大値を求める
    ans = 0
    for i in range(len(X)):
        if i+2*K+1 < len(X):
            ans = max(ans,X[i+2*K+1]-X[i])
        else:
            ans = max(ans,X[-1]-X[i])
    #Xの連続個数の累積和の最大値がNより大きい時、Nを出力する
    if ans > N:
        print(N)
    else:
        print(ans)

=======
Suggestion 10

def main():
    S = input()
    K = int(input())
    S_len = len(S)
    S_list = list(S)
    #print(S_list)
    X_count = 0
    X_count_list = []
    X_count_list.append(0)
    for i in range(S_len):
        if S_list[i] == "X":
            X_count += 1
        else:
            X_count_list.append(X_count)
            X_count = 0
    X_count_list.append(X_count)
    #print(X_count_list)
    X_count_list_len = len(X_count_list)
    #print(X_count_list_len)
    X_count_list_sum = 0
    #print(X_count_list_sum)
    for i in range(X_count_list_len):
        if i == 0 or i == X_count_list_len - 1:
            X_count_list_sum += X_count_list[i]
        else:
            if X_count_list[i] <= K:
                X_count_list_sum += X_count_list[i]
                K -= X_count_list[i]
            else:
                X_count_list_sum += K
                K = 0
    #print(X_count_list_sum)
    print(X_count_list_sum)
