Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '0':
            for j in range(i, N):
                if S[j] == '1':
                    ans = max(ans, j-i)
                    break
            else:
                ans = max(ans, N-i)
                break
        elif S[i] == '1':
            for j in range(i, N):
                if S[j] == '0':
                    ans = max(ans, j-i)
                    break
            else:
                ans = max(ans, N-i)
                break
    print(ans+K-1)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += 1
    if ans == 0:
        print(1)
        return
    if ans == N:
        print(N)
        return
    for i in range(N):
        if S[i] == '0':
            ans += 1
            break
    for i in range(N - 1, -1, -1):
        if S[i] == '0':
            ans += 1
            break
    ans = min(ans + 2 * K, N)
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    s = input()
    s = list(s)
    for i in range(k):
        for j in range(n-1):
            if s[j] == '0' and s[j+1] == '1':
                s[j] = '1'
                s[j+1] = '0'
    print(s.count('1'))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = input()
    S = S.replace("0", "1 0").replace("1", "0 1").split()
    S = [int(x) for x in S]
    N = len(S)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for i in range(N):
        left[i + 1] = left[i] + S[i]
        right[N - 1 - i] = right[N - i] + S[N - 1 - i]
    ans = 0
    for i in range(N + 1):
        l = max(0, i - 2 * K)
        r = min(N, i + 2 * K + 1)
        ans = max(ans, left[i] - left[l] + right[i] - right[r])
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    s = input()
    
    ans = 0
    for i in range(n):
        if s[i] == "1":
            continue
        cnt = 0
        for j in range(i, n):
            if s[j] == "0":
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
    
    print(min(n, ans + 2 * k))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
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
    #print

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = input()
    # 連続して逆立ちしている人の数を記録するリスト
    count_list = []
    # 連続して逆立ちしている人の数を記録する変数
    count = 0
    # 連続して直立している人の数を記録する変数
    zero_count = 0
    # 連続して逆立ちしている人の数を記録する
    for i in range(N):
        if S[i] == '1':
            count += 1
        else:
            count_list.append(count)
            count = 0
            zero_count += 1
    count_list.append(count)
    # 連続して直立している人の数がKより多い場合、
    # 連続して逆立ちしている人の数がK+1個以上になる
    if zero_count <= K:
        print(N)
        return
    # 連続して直立している人の数がKより少ない場合、
    # 連続して逆立ちしている人の数がK+1個以下になる
    else:
        # 連続して逆立ちしている人の数がK+1個以上になるようにする
        for i in range(zero_count - K):
            count_list.append(0)
        # 連続して逆立ちしている人の数を合計する
        count_list_sum = [0]
        for i in range(len(count_list)):
            count_list_sum.append(count_list_sum[-1] + count_list[i])
        # 連続して逆立ちしている人の数の最大値を求める
        max_count = 0
        for i in range(len(count_list_sum) - K - 1):
            max_count = max(max_count, count_list_sum[i+K+1] - count_list_sum[i])
        print(max_count)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    s = input()
    #print(n,k,s)
    s = s.replace('0','1').replace('1','0')
    #print(s)
    s = s.split('1')
    #print(s)
    s.sort()
    #print(s)
    s.reverse()
    #print(s)
    ans = 0
    for i in range(min(k,len(s))):
        ans += s[i]
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = input()

    # 1. 連続した0の数を数える
    # 2. 1の数がKより小さい場合は、0の数＋1
    # 3. 1の数がKより大きい場合は、K*2+1
    # 4. 1の数がKと同じ場合は、K*2

    # 1
    zero_count = 0
    zero_count_list = []
    for i in range(N):
        if S[i] == '0':
            zero_count += 1
        else:
            if zero_count > 0:
                zero_count_list.append(zero_count)
                zero_count = 0
    if zero_count > 0:
        zero_count_list.append(zero_count)

    # 2
    if len(zero_count_list) <= K:
        print(sum(zero_count_list) + len(zero_count_list))
        return

    # 3
    if len(zero_count_list) > K:
        print(K*2 + 1)
        return

    # 4
    if len(zero_count_list) == K:
        print(K*2)
        return

=======
Suggestion 10

def main():
    #入力
    n, k = map(int, input().split())
    s = input()
    #問題を解く
    result = 0
    #1. 0と1の連続した区間を数える
    #2. 0の区間を1つずつ変えていき、最大の区間の長さを数える
    #3. 1の区間の長さを数える
    #4. 3と2の和を取る
    #5. 1の区間の長さが1の場合は、2の値に1を足す
    #6. 5の値が答え
    #1. 0と1の連続した区間を数える
    s_list = []
    s_count = 0
    for i in range(n):
        if i == 0:
            s_count += 1
            continue
        if s[i] == s[i-1]:
            s_count += 1
        else:
            s_list.append(s_count)
            s_count = 1
    s_list.append(s_count)
    #print(s_list)
    #2. 0の区間を1つずつ変えていき、最大の区間の長さを数える
    s_list_len = len(s_list)
    s_0_max = 0
    for i in range(0, s_list_len, 2):
        s_0 = 0
        for j in range(k):
            if (i+2*j) > (s_list_len-1):
                break
            s_0 += s_list[i+2*j]
        s_0_max = max(s_0_max, s_0)
    #print(s_0_max)
    #3. 1の区間の長さを数える
    s_1 = 0
    for i in range(1, s_list_len, 2):
        s_1 += s_list[i]
    #print(s_1)
    #4. 3と2の和を取る
    result = s_1 + s_0_max
    #
