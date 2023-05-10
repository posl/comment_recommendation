Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,q = map(int,input().split())
    s = input()
    l = []
    r = []
    for i in range(q):
        l_i, r_i = map(int,input().split())
        l.append(l_i)
        r.append(r_i)

    for i in range(q):
        print(s[l[i]-1:r[i]-1].count('AC'))

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    s = input()
    a = [0] * n
    for i in range(n-1):
        if s[i] == 'A' and s[i+1] == 'C':
            a[i+1] = a[i] + 1
        else:
            a[i+1] = a[i]
    for i in range(q):
        l, r = map(int, input().split())
        print(a[r-1] - a[l-1])

=======
Suggestion 3

def main():
    N,Q = map(int,input().split())
    S = input()
    AC = [0]*N
    for i in range(1,N):
        if S[i-1] == "A" and S[i] == "C":
            AC[i] = AC[i-1] + 1
        else:
            AC[i] = AC[i-1]
    for i in range(Q):
        l,r = map(int,input().split())
        if l == 1:
            print(AC[r-1])
        else:
            print(AC[r-1] - AC[l-1])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    S = input()
    #print(N, Q, S)
    #print(len(S))
    #print(S[0:2])
    #print(S[2:4])
    #print(S[4:6])
    #print(S[6:8])
    #print(S[8:10])
    #print(S[10:12])
    #print(S[12:14])
    #print(S[14:16])
    #print(S[16:18])
    #print(S[18:20])
    #print(S[20:22])
    #print(S[22:24])
    #print(S[24:26])
    #print(S[26:28])
    #print(S[28:30])
    #print(S[30:32])
    #print(S[32:34])
    #print(S[34:36])
    #print(S[36:38])
    #print(S[38:40])
    #print(S[40:42])
    #print(S[42:44])
    #print(S[44:46])
    #print(S[46:48])
    #print(S[48:50])
    #print(S[50:52])
    #print(S[52:54])
    #print(S[54:56])
    #print(S[56:58])
    #print(S[58:60])
    #print(S[60:62])
    #print(S[62:64])
    #print(S[64:66])
    #print(S[66:68])
    #print(S[68:70])
    #print(S[70:72])
    #print(S[72:74])
    #print(S[74:76])
    #print(S[76:78])
    #print(S[78:80])
    #print(S[80:82])
    #print(S[82:84])
    #print(S[84:86])
    #print(S[86:88])
    #print(S[88:90])
    #print(S[90:92])
    #print(S[92:94])
    #print(S[94:96])
    #print(S[96:98])
    #print(S[98:100])
    #print(S[100:102])
    #print(S[102:

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    S = input()
    count = [0] * (N + 1)
    for i in range(N):
        count[i + 1] = count[i]
        if S[i] == 'A' and S[i + 1] == 'C':
            count[i + 1] += 1
    for i in range(Q):
        l, r = map(int, input().split())
        print(count[r - 1] - count[l - 1])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    S = input()
    #print(N, Q)
    #print(S)
    #print(S[3:7])
    #print(S[2:3])
    #print(S[1:8])
    #print(S[0:8])
    #print(S[0:7])
    #print(S[0:6])
    #print(S[0:5])
    #print(S[0:4])
    #print(S[0:3])
    #print(S[0:2])
    #print(S[0:1])
    #print(S[0:0])
    #print(S[0:8].count('AC'))
    #print(S[0:7].count('AC'))
    #print(S[0:6].count('AC'))
    #print(S[0:5].count('AC'))
    #print(S[0:4].count('AC'))
    #print(S[0:3].count('AC'))
    #print(S[0:2].count('AC'))
    #print(S[0:1].count('AC'))
    #print(S[0:0].count('AC'))
    #print(S[1:8].count('AC'))
    #print(S[2:3].count('AC'))
    #print(S[3:7].count('AC'))
    #print(S[0:8].count('AC'))
    #print(S[0:7].count('AC'))
    #print(S[0:6].count('AC'))
    #print(S[0:5].count('AC'))
    #print(S[0:4].count('AC'))
    #print(S[0:3].count('AC'))
    #print(S[0:2].count('AC'))
    #print(S[0:1].count('AC'))
    #print(S[0:0].count('AC'))
    #print(S[1:8].count('AC'))
    #print(S[2:3].count('AC'))
    #print(S[3:7].count('AC'))
    #print(S[0:8].count('AC'))
    #print(S[0:7].count('AC'))
    #print(S[0:6].count('AC'))
    #print(S[0:5].count

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    s = input()
    ac = [0] * n
    for i in range(n-1):
        ac[i+1] = ac[i]
        if s[i] == 'A' and s[i+1] == 'C':
            ac[i+1] += 1
    for i in range(q):
        l, r = map(int, input().split())
        print(ac[r-1] - ac[l-1])

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    S = input()

    AC_count = [0] * (N + 1)
    for i in range(1, N):
        AC_count[i + 1] = AC_count[i]
        if S[i - 1] == 'A' and S[i] == 'C':
            AC_count[i + 1] += 1

    for _ in range(Q):
        l, r = map(int, input().split())
        print(AC_count[r] - AC_count[l])

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    S = input()
    AC = [0] * N
    for i in range(1, N):
        if S[i-1] == 'A' and S[i] == 'C':
            AC[i] = AC[i-1] + 1
        else:
            AC[i] = AC[i-1]
    for i in range(Q):
        l, r = map(int, input().split())
        print(AC[r-1] - AC[l-1])

=======
Suggestion 10

def main():
    n,q=map(int,input().split())
    s=input()
    ac=[0]*(n+1)
    for i in range(1,n):
        ac[i+1]=ac[i]
        if s[i-1:i+1]=="AC":
            ac[i+1]+=1
    for i in range(q):
        l,r=map(int,input().split())
        print(ac[r]-ac[l])
