Synthesizing 10/10 solutions

=======
Suggestion 1

def countAC(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'A' and s[i+1] == 'C':
            count += 1
    return count

n, q = map(int, input().split())
s = input()
for i in range(q):
    l, r = map(int, input().split())
    print(countAC(s[l-1:r]))

=======
Suggestion 2

def main():
    n,q = map(int,input().split())
    s = input()
    l = []
    for i in range(q):
        l.append(list(map(int,input().split())))
    
    for i in range(q):
        print(s.count('AC',l[i][0]-1,l[i][1]))

=======
Suggestion 3

def solve(s, l, r):
    count = 0
    for i in range(l-1, r):
        if s[i:i+2] == 'AC':
            count += 1
    return count

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    S = input()
    S = list(S)
    #print(N, Q, S)
    #print(S[1:3])
    #print(S[0:8])
    #print(S[0:9])
    #print(S[0:10])
    #print(S[0:11])
    #print(S[0:12])
    #print(S[0:13])
    #print(S[0:14])
    #print(S[0:15])
    #print(S[0:16])
    #print(S[0:17])
    #print(S[0:18])
    #print(S[0:19])
    #print(S[0:20])
    #print(S[0:21])
    #print(S[0:22])
    #print(S[0:23])
    #print(S[0:24])
    #print(S[0:25])
    #print(S[0:26])
    #print(S[0:27])
    #print(S[0:28])
    #print(S[0:29])
    #print(S[0:30])
    #print(S[0:31])
    #print(S[0:32])
    #print(S[0:33])
    #print(S[0:34])
    #print(S[0:35])
    #print(S[0:36])
    #print(S[0:37])
    #print(S[0:38])
    #print(S[0:39])
    #print(S[0:40])
    #print(S[0:41])
    #print(S[0:42])
    #print(S[0:43])
    #print(S[0:44])
    #print(S[0:45])
    #print(S[0:46])
    #print(S[0:47])
    #print(S[0:48])
    #print(S[0:49])
    #print(S[0:50])
    #print(S[0:51])
    #print(S[0:52])
    #print(S[0:53])
    #print(S[0:54])
    #print(S[0:55])
    #print(S[0:56])
    #print(S[0:57])
    #print(S[0:

=======
Suggestion 5

def countAC(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'A' and s[i+1] == 'C':
            count += 1
    return count

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    S = input()
    lr_list = []
    for i in range(Q):
        lr_list.append(list(map(int, input().split())))
    for i in range(Q):
        l = lr_list[i][0]
        r = lr_list[i][1]
        count = 0
        for j in range(l-1, r-1):
            if S[j] == 'A' and S[j+1] == 'C':
                count += 1
        print(count)

=======
Suggestion 7

def get_input():
    n, q = [int(i) for i in input().split()]
    s = input()
    return n, q, s

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    S = input()
    lr = []
    for i in range(Q):
        lr.append(list(map(int, input().split())))
    ac = [0] * N
    for i in range(1, N):
        if S[i - 1] == 'A' and S[i] == 'C':
            ac[i] = ac[i - 1] + 1
        else:
            ac[i] = ac[i - 1]
    for i in range(Q):
        print(ac[lr[i][1] - 1] - ac[lr[i][0] - 1])

=======
Suggestion 9

def solve():
    N, Q = map(int, input().split())
    S = input()
    AC = [0] * N
    for i in range(N - 1):
        if S[i] == 'A' and S[i + 1] == 'C':
            AC[i] = 1
    for i in range(N - 2, -1, -1):
        AC[i] += AC[i + 1]
    for i in range(Q):
        l, r = map(int, input().split())
        print(AC[l - 1] - AC[r - 1])

=======
Suggestion 10

def problem122_c():
    n,q = map(int,input().split())
    s = input()
    l = []
    r = []
    for i in range(q):
        l_i,r_i = map(int,input().split())
        l.append(l_i)
        r.append(r_i)
    for i in range(q):
        print(s[l[i]-1:r[i]].count('AC'))
