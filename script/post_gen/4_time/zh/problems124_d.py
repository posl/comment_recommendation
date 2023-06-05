Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    s = input()
    ans = 0
    cnt = 0
    for i in range(n):
        if s[i] == '0':
            cnt += 1
        else:
            if k > 0:
                k -= 1
                cnt += 1
            else:
                cnt -= 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

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
Suggestion 3

def main():
    n, k = map(int, input().split())
    s = input()
    # 0,1の状態を数える
    cnt = [0]
    for i in range(n):
        cnt.append(cnt[-1] + int(s[i]))
    # 01の状態を数える
    cnt2 = [0]
    for i in range(n):
        cnt2.append(cnt2[-1] + 1 if s[i] == '0' else cnt2[-1])
    # 01の状態から、K回の操作で得られる01の状態の最大値を求める
    ans = 0
    for i in range(n):
        l = 0
        r = min(n, i + k * 2 + 1)
        while r - l > 1:
            m = (l + r) // 2
            if cnt2[m] - cnt2[i] <= k:
                l = m
            else:
                r = m
        ans = max(ans, cnt[l] - cnt[i])
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    s = input()
    cnt = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1
    print(min(n-1, cnt+2*k))

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    S = input()
    #print(N,K)
    #print(S)
    s_list = list(S)
    #print(s_list)
    #print(s_list[0])
    #print(s_list[1])
    #print(s_list[2])
    #print(s_list[3])
    #print(s_list[4])
    #print(s_list[5])
    #print(s_list[6])
    #print(s_list[7])
    #print(s_list[8])
    #print(s_list[9])
    #print(s_list[10])
    #print(s_list[11])
    #print(s_list[12])
    #print(s_list[13])
    #print(s_list[14])
    #print(s_list[15])
    #print(s_list[16])
    #print(s_list[17])
    #print(s_list[18])
    #print(s_list[19])
    #print(s_list[20])
    #print(s_list[21])
    #print(s_list[22])
    #print(s_list[23])
    #print(s_list[24])
    #print(s_list[25])
    #print(s_list[26])
    #print(s_list[27])
    #print(s_list[28])
    #print(s_list[29])
    #print(s_list[30])
    #print(s_list[31])
    #print(s_list[32])
    #print(s_list[33])
    #print(s_list[34])
    #print(s_list[35])
    #print(s_list[36])
    #print(s_list[37])
    #print(s_list[38])
    #print(s_list[39])
    #print(s_list[40])
    #print(s_list[41])
    #print(s_list[42])
    #print(s_list[43])
    #print(s_list[44])
    #print(s_list[45])
    #print(s_list[46])
    #print(s_list[47])
    #print(s_list[48])
    #print(s_list[49])
    #print(s_list[50])
    #print(s_list[51])
    #print(s_list[52])
    #print(s_list[53])
    #print(s_list[54])
    #print(s_list[55])
    #print(s_list[56])
    #print

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for l in range(N):
        for r in range(l, N):
            if S[r] == "0":
                K -= 1
            if K < 0:
                if S[l] == "0":
                    K += 1
                break
            ans = max(ans, r - l + 1)
    print(ans)

=======
Suggestion 7

def main():
    print("请在此编写代码，通过本机测试样例！")
    pass

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    S = list(input())
    print(S)
    #print(N,K)
    #print(S)

=======
Suggestion 9

def solve():
    n, k = map(int, input().split())
    s = input()
    result = 0
    for i in range(n):
        if s[i] == "0":
            result += 1
    result += min(k, n - 1)
    print(result)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    s = list(input())
    cnt = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            cnt += 1
    ans = min(n - 1, cnt + 2 * k)
    print(ans)
