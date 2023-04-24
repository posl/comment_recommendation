Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    s = input()
    cnt = 0
    for i in range(n-1):
        if s[i] != s[i+1]:
            cnt += 1
    print(min(n-1, cnt + 2*k))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = input()
    S = S.replace('1', '2')
    S = S.replace('0', '1')
    S = S.replace('2', '0')
    S = list(S)
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(i, N):
            if S[j] == '1':
                cnt += 1
                if cnt > K:
                    break
            else:
                if cnt == K:
                    break
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    cnt = 0
    for i in range(N):
        if S[i] == '0':
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(min(N-1, ans+2*K))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = input()
    cnt = 0
    ans = 0
    for i in range(N):
        if S[i] == '0':
            cnt += 1
            if cnt == K + 1:
                ans += 1
                cnt -= 1
        else:
            ans += cnt
            cnt = 0
    ans += cnt
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += 1
            if i + 1 < N and S[i + 1] == '1':
                ans += 1
    if ans == 0:
        print(N - 1)
    else:
        print(min(ans + 2 * K, N))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = input()

    ans = 0
    for i in range(N):
        if i == 0:
            if S[i] == '0':
                ans = 1
            else:
                ans = 0
        else:
            if S[i] == '0':
                ans += 1
            else:
                ans = 0

        if ans >= K:
            print(N)
            exit()

    print(ans)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    S = list(input())
    for i in range(K):
        if S[i] == "0":
            S[i] = "1"
        else:
            S[i] = "0"
        if S[i] == "0":
            S[i] = "1"
        else:
            S[i] = "0"
    print(N - S.count("0"))

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "1":
            ans += 1
    ans = min(ans+2*K,N)
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = input()

    # 0, 1 それぞれの区間の長さのリストを作る
    # 例: S = 00010 のとき
    # 0 の区間: [3, 1]
    # 1 の区間: [1]
    intervals = []
    current = S[0]
    count = 0
    for s in S:
        if s == current:
            count += 1
        else:
            intervals.append(count)
            count = 1
            current = s
    intervals.append(count)

    # 0, 1 それぞれの区間の長さのリストから、
    # 0 の区間の長さのリストを作る
    # 例: S = 00010 のとき
    # 0 の区間: [3, 1]
    intervals_0 = []
    for i in range(0, len(intervals), 2):
        intervals_0.append(intervals[i])

    # 0 の区間の長さのリストから、
    # 0 の区間の長さのリストのうち、
    # K 個を選んで足した値の最大値を求める
    # 例: K = 1 のとき
    # 0 の区間: [3, 1]
    # 0 の区間の長さのリストのうち、1 個を選んで足した値の最大値: 3 + 1 = 4
    # 例: K = 2 のとき
    # 0 の区間: [3, 1]
    # 0 の区間の長さのリストのうち、2 個を選んで足した値の最大値: 3 + 1 = 4
    ans = 0
    for i in range(min(K, len(intervals_0))):
        ans += intervals_0[i]
    for i in range(min(K, len(intervals_0)) - 1,

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    S = input()
    # 0 と 1 の間に 1 を挿入して 0 と 1 の数を揃える
    # 0 と 1 の数は K + 1 以下のため、全探索できる
    S = S.replace("01", "0 1").replace("10", "1 0").split()
    # 0 と 1 の数
    num = [0] * (len(S) + 1)
    for i in range(len(S)):
        num[i + 1] = num[i] + int(S[i])
    # 0 と 1 の数の差
    diff = [0] * (len(S) + 1)
    for i in range(len(S)):
        diff[i + 1] = diff[i] + int(S[i]) * 2 - 1
    # 0 と 1 の数の差の最大値
    ans = 0
    for i in range(len(S) + 1):
        for j in range(i, len(S) + 1):
            if num[j] - num[i] <= K:
                ans = max(ans, diff[j] - diff[i])
    print(ans)
