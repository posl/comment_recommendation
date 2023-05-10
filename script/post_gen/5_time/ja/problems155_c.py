Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort()
    s_count = [0] * n
    for i in range(n):
        s_count[i] = s.count(s[i])
    max_s_count = max(s_count)
    for i in range(n):
        if s_count[i] == max_s_count:
            print(s[i])

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    #print(S)
    max = 0
    cnt = 0
    for i in range(1,N):
        if S[i-1] == S[i]:
            cnt += 1
            if cnt > max:
                max = cnt
        else:
            cnt = 0
    #print(max)
    cnt = 0
    for i in range(1,N):
        if S[i-1] == S[i]:
            cnt += 1
            if cnt == max:
                print(S[i])
        else:
            cnt = 0

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    S.sort()
    S.append('')

    ans = []
    cnt = 1
    for i in range(N):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            if cnt == 1:
                pass
            else:
                ans.append(S[i])
            cnt = 1

    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    #print(s)
    cnt = 1
    max_cnt = 0
    max_str = []
    for i in range(1,n):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                max_str.clear()
                max_str.append(s[i-1])
            elif cnt == max_cnt:
                max_str.append(s[i-1])
            cnt = 1
    if cnt > max_cnt:
        max_cnt = cnt
        max_str.clear()
        max_str.append(s[n-1])
    elif cnt == max_cnt:
        max_str.append(s[n-1])
    for i in range(len(max_str)):
        print(max_str[i])

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    #print(S)
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
    #print(S[65

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    ans = []
    cnt = 1
    for i in range(1,N):
        if S[i] == S[i-1]:
            cnt += 1
        else:
            if cnt > 1:
                ans.append(S[i-1])
            cnt = 1
    if cnt > 1:
        ans.append(S[N-1])
    for i in ans:
        print(i)

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    S.append("")
    c = 1
    for i in range(N):
        if S[i] != S[i+1]:
            if c > 1:
                print(S[i])
            c = 1
        else:
            c += 1

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    count = 1
    max_count = 0
    ans = []
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
        else:
            if max_count < count:
                ans = []
                ans.append(S[i])
                max_count = count
                count = 1
            elif max_count == count:
                ans.append(S[i])
                count = 1
            else:
                count = 1
    if max_count < count:
        ans = []
        ans.append(S[N-1])
        max_count = count
    elif max_count == count:
        ans.append(S[N-1])
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    cnt = 1
    ans = []
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            if cnt == max_cnt:
                ans.append(S[i])
            elif cnt > max_cnt:
                ans = [S[i]]
                max_cnt = cnt
            cnt = 1
    if cnt == max_cnt:
        ans.append(S[-1])
    elif cnt > max_cnt:
        ans = [S[-1]]
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 10

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    max = 0
    for x in d:
        if d[x] > max:
            max = d[x]
    for x in sorted(d):
        if d[x] == max:
            print(x)
