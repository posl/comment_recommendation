Synthesizing 10/10 solutions

=======
Suggestion 1

def countAC(s, l, r):
    count = 0
    for i in range(l, r):
        if s[i] == 'A' and s[i+1] == 'C':
            count += 1
    return count

=======
Suggestion 2

def solve():
    N,Q = map(int,input().split())
    S = input()
    l = [0]*N
    for i in range(N-1):
        if S[i:i+2] == 'AC':
            l[i] = 1
    for i in range(N-1):
        l[i+1] += l[i]
    for _ in range(Q):
        l_i,r_i = map(int,input().split())
        print(l[r_i-2]-l[l_i-1])
solve()

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    s = input()
    l = [0] * n
    for i in range(n - 1):
        if s[i] == 'A' and s[i + 1] == 'C':
            l[i + 1] = l[i] + 1
        else:
            l[i + 1] = l[i]
    for i in range(q):
        lft, rght = map(int, input().split())
        print(l[rght - 1] - l[lft - 1])

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    s = input()
    l = []
    r = []
    for i in range(q):
        l1, r1 = map(int, input().split())
        l.append(l1)
        r.append(r1)

    for i in range(q):
        print(s[l[i]-1:r[i]].count("AC"))

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    S = input()
    T = [0] * (N + 1)
    for i in range(1, N):
        if S[i-1] == 'A' and S[i] == 'C':
            T[i+1] = T[i] + 1
        else:
            T[i+1] = T[i]
    for i in range(Q):
        l, r = map(int, input().split())
        print(T[r] - T[l])

=======
Suggestion 6

def main():
    N,Q=map(int,input().split())
    S=input()
    l=[0]*N
    for i in range(1,N):
        if S[i-1]=='A' and S[i]=='C':
            l[i]=l[i-1]+1
        else:
            l[i]=l[i-1]
    for i in range(Q):
        l_i,r_i=map(int,input().split())
        print(l[r_i-1]-l[l_i-1])

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    s = input()
    t = [0]
    for i in range(1, n):
        t.append(t[i-1])
        if s[i-1] == 'A' and s[i] == 'C':
            t[i] += 1
    for _ in range(q):
        l, r = map(int, input().split())
        print(t[r-1]-t[l-1])

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    s = input()
    #print(n, q, s)
    #print(s[2:7])
    #print(s[1:3])
    #print(s[0:8])
    #print(s[0:0])
    #print(s[0:1])
    #print(s[0:2])
    #print(s[0:3])
    #print(s[0:4])
    #print(s[0:5])
    #print(s[0:6])
    #print(s[0:7])
    #print(s[0:8])
    #print(s[0:9])
    #print(s[0:10])
    #print(s[0:11])
    #print(s[0:12])
    #print(s[0:13])
    #print(s[0:14])
    #print(s[0:15])
    #print(s[0:16])
    #print(s[0:17])
    #print(s[0:18])
    #print(s[0:19])
    #print(s[0:20])
    #print(s[0:21])
    #print(s[0:22])
    #print(s[0:23])
    #print(s[0:24])
    #print(s[0:25])
    #print(s[0:26])
    #print(s[0:27])
    #print(s[0:28])
    #print(s[0:29])
    #print(s[0:30])
    #print(s[0:31])
    #print(s[0:32])
    #print(s[0:33])
    #print(s[0:34])
    #print(s[0:35])
    #print(s[0:36])
    #print(s[0:37])
    #print(s[0:38])
    #print(s[0:39])
    #print(s[0:40])
    #print(s[0:41])
    #print(s[0:42])
    #print(s[0:43])
    #print(s[0:44])
    #print(s[0:45])
    #print(s[0:46])
    #print(s[0:47])
    #print(s[0:48])
    #print(s

=======
Suggestion 9

def solve():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * N
    for i in range(1, N):
        l[i] = l[i-1]
        if S[i-1] == "A" and S[i] == "C":
            l[i] += 1
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i-1]-l[l_i-1])

solve()

=======
Suggestion 10

def solve():
    N, Q = map(int, input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)

    ac = [0] * (N + 1)
    for i in range(N):
        if i == 0:
            continue
        if S[i - 1] == "A" and S[i] == "C":
            ac[i + 1] = ac[i] + 1
        else:
            ac[i + 1] = ac[i]

    for i in range(Q):
        print(ac[r[i]] - ac[l[i]])
