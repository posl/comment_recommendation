Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N+1)
    for i in range(1, N):
        l[i+1] = l[i]
        if S[i-1:i+1] == "AC":
            l[i+1] += 1
    for i in range(Q):
        a, b = map(int, input().split())
        print(l[b] - l[a])

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    S = input()
    #print(N, Q, S)
    #print(type(N), type(Q), type(S))
    #print(S[0:2])
    #print(S[0:2].count('AC'))
    #print(S[1:3].count('AC'))
    #print(S[2:4].count('AC'))
    #print(S[3:5].count('AC'))
    #print(S[4:6].count('AC'))
    #print(S[5:7].count('AC'))
    #print(S[6:8].count('AC'))
    #print(S[7:9].count('AC'))
    #print(S[8:10].count('AC'))
    #print(S[9:11].count('AC'))
    #print(S[10:12].count('AC'))
    #print(S[11:13].count('AC'))
    #print(S[12:14].count('AC'))
    #print(S[13:15].count('AC'))
    #print(S[14:16].count('AC'))
    #print(S[15:17].count('AC'))
    #print(S[16:18].count('AC'))
    #print(S[17:19].count('AC'))
    #print(S[18:20].count('AC'))
    #print(S[19:21].count('AC'))
    #print(S[20:22].count('AC'))
    #print(S[21:23].count('AC'))
    #print(S[22:24].count('AC'))
    #print(S[23:25].count('AC'))
    #print(S[24:26].count('AC'))
    #print(S[25:27].count('AC'))
    #print(S[26:28].count('AC'))
    #print(S[27:29].count('AC'))
    #print(S[28:30].count('AC'))
    #print(S[29:31].count('AC'))
    #print(S[30:32].count('AC'))
    #print(S[31:33].count('AC'))
    #print(S[32:34].count('AC'))
    #print(S[33:35].count('AC'))
    #print(S[34:36].

=======
Suggestion 3

def countAC(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i] == 'A' and s[i + 1] == 'C':
            count += 1
    return count

=======
Suggestion 4

def countAC(S):
    count = 0
    for i in range(len(S)-1):
        if S[i]+S[i+1] == 'AC':
            count += 1
    return count

=======
Suggestion 5

def count_ac(s):
    cnt = 0
    for i in range(len(s) - 1):
        if s[i] == 'A' and s[i + 1] == 'C':
            cnt += 1
    return cnt

=======
Suggestion 6

def problem122_c():
    N, Q = map(int, input().split())
    S = input()
    #print(N, Q, S)
    #print(S[3:7].count("AC"))
    #print(S[2:3].count("AC"))
    #print(S[1:8].count("AC"))
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        #print(l_i, r_i)
        print(S[l_i-1:r_i].count("AC"))

problem122_c()

=======
Suggestion 7

def solve(S, l, r):
    count = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            if S[i:j] == "AC":
                count += 1
    return count

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        l1, r1 = map(int, input().split())
        l.append(l1)
        r.append(r1)
    for i in range(Q):
        print(S[l[i]-1:r[i]].count("AC"))

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    s = input()
    # 1. 生成累积和列表
    acc = [0]
    for i in range(1, n):
        if s[i - 1] == 'A' and s[i] == 'C':
            acc.append(acc[i - 1] + 1)
        else:
            acc.append(acc[i - 1])

    # 2. 解决每个查询
    for _ in range(q):
        l, r = map(int, input().split())
        print(acc[r - 1] - acc[l - 1])

=======
Suggestion 10

def solve():
    N, Q = map(int, input().split())
    S = input()
    cnt = [0] * N
    for i in range(1, N):
        cnt[i] = cnt[i-1]
        if S[i-1:i+1] == 'AC':
            cnt[i] += 1
    for _ in range(Q):
        l, r = map(int, input().split())
        print(cnt[r-1] - cnt[l-1])
solve()
