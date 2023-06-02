Synthesizing 7/10 solutions

=======
Suggestion 1

def get_input():
    n, k = map(int, input().split())
    s = input()
    return n, k, s

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    #print(S[0:2])
    #print(S[2:4])
    #print(S[0:2] == S[2:4])
    #print(S[0:1] == S[1:2])
    #print(S[0:1] == S[2:3])
    #print(S[0:1] == S[3:4])
    #print(S[0:1] == S[4:5])
    #print(S[0:1] == S[5:6])
    #print(S[0:1] == S[6:7])
    #print(S[0:1] == S[7:8])
    #print(S[0:1] == S[8:9])
    #print(S[0:1] == S[9:10])
    #print(S[0:1] == S[10:11])
    #print(S[0:1] == S[11:12])
    #print(S[0:1] == S[12:13])
    #print(S[0:1] == S[13:14])
    #print(S[0:1] == S[14:15])
    #print(S[0:1] == S[15:16])
    #print(S[0:1] == S[16:17])
    #print(S[0:1] == S[17:18])
    #print(S[0:1] == S[18:19])
    #print(S[0:1] == S[19:20])
    #print(S[0:1] == S[20:21])
    #print(S[0:1] == S[21:22])
    #print(S[0:1] == S[22:23])
    #print(S[0:1] == S[23:24])
    #print(S[0:1] == S[24:25])
    #print(S[0:1] == S[25:26])
    #print(S[0:1] == S[26:27])
    #print(S[0:1] == S[27:28])
    #print(S[0

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = input()

    # 0と1の切り替わりをカウントする
    # 1 0 1 1 0 1 0 1 1 0 0 1 1 1
    #  1 1 1 2 2 2 3 3 3 4 4 4 4
    #  1 1 1 2 2 2 3 3 3 3 3 3 3
    #  1 1 1 2 2 2 3 3 3 3 3 3 3
    #  1 1 1 2 2 2 3 3 3 3 3 3 3
    #  1 1 1 2 2 2 3 3 3 3 3 3 3
    #  1 1 1 2 2 2 3 3 3 3 3 3 3
    #  1 1 1 2 2 2 3 3 3 3 3 3 3
    #  1 1 1 2 2 2 3 3 3 3 3 3 3
    #  1 1 1 2 2 2 3 3 3 3 3 3 3
    #  1 1 1 2 2 2 2 2 2 2 2 2 2
    #  1 1 1 2 2 2 2 2 2 2 2 2 2
    #  1 1 1 2 2 2 2 2 2 2 2 2 2
    #  1 1 1 2 2 2 2 2 2 2 2 2 2

    # 1 0 1 0 1 0 1 0 1 0 1 0 1 0
    #  1 1 2

=======
Suggestion 4

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
Suggestion 5

def main():
    N,K = map(int,input().split())
    s = input()
    #print(N,K,s)
    s = list(s)
    #print(s)
    ans = 0
    for i in range(N-1):
        if s[i] == s[i+1]:
            ans += 1
    ans = min(ans+2*K,N-1)
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    cnt = 0
    for i in range(N):
        if S[i] == "0":
            cnt += 1
        else:
            if K > 0:
                K -= 1
                cnt += 1
            else:
                cnt -= 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = input()
    S = list(S)
    cnt = 0
    if S[0] == '0':
        cnt += 1
    for i in range(N-1):
        if S[i] == '1' and S[i+1] == '0':
            cnt += 1
    if S[-1] == '0':
        cnt += 1
    print(min(cnt+2*K, N)-1)
