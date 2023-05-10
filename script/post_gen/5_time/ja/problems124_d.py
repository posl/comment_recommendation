Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 標準入力の受け取り
    N,K = map(int,input().split())
    S = input()
    # 0の連続個数をカウント
    zero = 0
    zero_list = []
    for i in range(N):
        if S[i] == '0':
            zero += 1
        else:
            zero_list.append(zero)
            zero = 0
    zero_list.append(zero)
    # 0の連続個数のリストから、K回の指示で反転できる最大値を求める
    if len(zero_list) <= K:
        print(N)
    else:
        max_zero = 0
        for i in range(len(zero_list)-K):
            zero_sum = sum(zero_list[i:i+K+1])
            if zero_sum > max_zero:
                max_zero = zero_sum
        print(max_zero)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)

    # 0の連続数をカウント
    l = 0
    cnt = 0
    zero_cnt = []
    for i in range(N):
        if S[i] == '0':
            l += 1
        else:
            zero_cnt.append(l)
            l = 0
        if i == N-1:
            zero_cnt.append(l)
    #print(zero_cnt)

    # 0の連続数がK回以上ある場合
    if len(zero_cnt) > K:
        # 0の連続数の合計からK回分の0を引く
        zero_cnt_sum = sum(zero_cnt)
        for i in range(K):
            zero_cnt_sum -= zero_cnt[i]
        #print(zero_cnt_sum)
        # 0の連続数の合計からK回分の0を引いた数が答え
        print(zero_cnt_sum)
    # 0の連続数がK回以下の場合
    else:
        # 0の連続数の合計が答え
        print(sum(zero_cnt))

=======
Suggestion 3

def solve():
    n, k = map(int, input().split())
    s = input()

    # 0の区間を求める
    # 1の区間を求める
    # 0の区間の両端を1の区間の両端とするような区間を求める
    # 1の区間の両端を0の区間の両端とするような区間を求める
    # 0の区間の両端を1の区間の両端とするような区間のうち、最も長いものを求める
    # 1の区間の両端を0の区間の両端とするような区間のうち、最も長いものを求める
    # 0の区間の両端を1の区間の両端とするような区間のうち、最も長いものを求める
    # 1の区間の両端を0の区間の両端とするような区間のうち、最も長いものを求める
    # 0の区間の両端を1の区間の両端とするような区間のうち、最も長いものを求める
    # 1の区間の両端を0の区間の両端とするような区間のうち、最も長いものを求める
    # 0の区間の両端を1の区間の両端とするような区間のうち、最も長いものを求める
    # 1の区間の両端を0の区間の両端とするような区間のうち、最も長いものを求める
    # 0の区間の両端を1の区間の両端とするような区間のうち、最も長いものを求める
    # 1の区

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = input().rstrip()
    ans = 0
    cnt = 0
    for i in range(N):
        if S[i] == "0":
            cnt += 1
        else:
            if K > 0:
                K -= 1
            else:
                while S[i] == "1":
                    i += 1
                i -= 1
                ans = max(ans, cnt)
                cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    s = input()
    # 0の数をカウント
    zero_count = 0
    # 0の数をカウントするリスト
    zero_count_list = []
    # 0をカウントしていく
    for i in range(n):
        if s[i] == "0":
            zero_count += 1
        else:
            zero_count_list.append(zero_count)
            zero_count = 0
    zero_count_list.append(zero_count)
    # 0をカウントするリストを作成
    zero_count_list.sort(reverse=True)
    # 0をカウントするリストの先頭からk個の合計値を求める
    ans = 0
    for i in range(k):
        ans += zero_count_list[i]
    print(ans)

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    cnt = 0
    prev = '0'
    for i in range(N):
        if S[i] == '0':
            if prev == '1':
                cnt += 1
            else:
                cnt = 1
        else:
            cnt += 1
        if cnt > ans:
            ans = cnt
        prev = S[i]
    if K > 0:
        cnt = 0
        prev = '1'
        for i in range(N):
            if S[i] == '0':
                if prev == '1':
                    cnt += 1
                else:
                    cnt = 1
            else:
                cnt += 1
            if cnt > ans:
                ans = cnt
            prev = S[i]
    if ans > N:
        ans = N
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    #print(len(S))
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62])
    #print(S[63])
    #print(S[64])
    #print(S[65])
    #print(S

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    S = input()
    S = list(S)
    #print(N,K,S)
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62])
    #print(S[63])
    #print(S[64])
    #print(S[65])
    #print(S[66])

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    s = [int(i) for i in input()]
    ans = 0
    cnt = 0
    for i in range(n):
        if s[i] == 0:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    ans += k
    if ans > n:
        ans = n
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    #print(type(N), type(K), type(S))
    #print(len(S))
    #print(S[2])
    #print(S[1:3])
    #print(S[0:3])
    #print(S[0:4])
    #print(S[0:5])
    #print(S[0:6])
    #print(S[0:7])
    #print(S[0:8])
    #print(S[0:9])
    #print(S[0:10])
    #print(S[0:11])
    #print(S[0:12])
    #print(S[0:13])
    #print(S[0:14])

    #print(S[0:1])
    #print(S[0:2])
    #print(S[0:3])
    #print(S[0:4])
    #print(S[0:5])
    #print(S[0:6])
    #print(S[0:7])
    #print(S[0:8])
    #print(S[0:9])
    #print(S[0:10])
    #print(S[0:11])
    #print(S[0:12])
    #print(S[0:13])
    #print(S[0:14])
    #print(S[0:15])

    #print(S[0:1])
    #print(S[0:2])
    #print(S[0:3])
    #print(S[0:4])
    #print(S[0:5])
    #print(S[0:6])
    #print(S[0:7])
    #print(S[0:8])
    #print(S[0:9])
    #print(S[0:10])
    #print(S[0:11])
    #print(S[0:12])
    #print(S[0:13])
    #print(S[0:14])
    #print(S[0:15])
    #print(S[0:16])

    #print(S[0:1])
    #print(S[0:2])
    #print(S[0:3])
    #print(S[0:4])
    #print(S[0:5])
    #print(S[0
