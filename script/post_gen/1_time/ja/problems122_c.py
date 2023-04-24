Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    S = input()
    AC = [0] * (N + 1)
    for i in range(1, N):
        if S[i - 1] == 'A' and S[i] == 'C':
            AC[i + 1] = AC[i] + 1
        else:
            AC[i + 1] = AC[i]
    for i in range(Q):
        l, r = map(int, input().split())
        print(AC[r] - AC[l])

=======
Suggestion 2

def main():
    N,Q = map(int,input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        l_i,r_i = map(int,input().split())
        l.append(l_i)
        r.append(r_i)
    for i in range(Q):
        print(S[l[i]-1:r[i]].count("AC"))

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N + 1)
    for i in range(N):
        l[i + 1] = l[i]
        if S[i:i + 2] == 'AC':
            l[i + 1] += 1
    for _ in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i - 1] - l[l_i - 1])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    S = input()
    AC = [0] * (N + 1)
    for i in range(1, N):
        if S[i-1] == "A" and S[i] == "C":
            AC[i] = AC[i-1] + 1
        else:
            AC[i] = AC[i-1]
    for _ in range(Q):
        l, r = map(int, input().split())
        print(AC[r-1] - AC[l-1])

=======
Suggestion 5

def main():
    n,q = map(int,input().split())
    s = input()
    ac = [0]*n
    for i in range(n-1):
        if s[i] == 'A' and s[i+1] == 'C':
            ac[i] = 1
    for i in range(1,n):
        ac[i] += ac[i-1]
    for i in range(q):
        l,r = map(int,input().split())
        print(ac[r-1]-ac[l-1])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    S = input()
    AC = [0] * (N + 1)
    for i in range(N):
        if S[i] == 'A' and S[i+1] == 'C':
            AC[i+1] = AC[i] + 1
        else:
            AC[i+1] = AC[i]
    for i in range(Q):
        l, r = map(int, input().split())
        print(AC[r-1] - AC[l-1])

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    S = input()
    AC_count = [0] * (N+1)
    for i in range(N):
        if S[i:i+2] == 'AC':
            AC_count[i+1] = AC_count[i] + 1
        else:
            AC_count[i+1] = AC_count[i]
    for i in range(Q):
        l, r = map(int, input().split())
        print(AC_count[r-1] - AC_count[l-1])

=======
Suggestion 8

def main():
    N,Q = map(int,input().split())
    S = input()
    AC = [0] * N
    for i in range(1,N):
        if S[i-1] == 'A' and S[i] == 'C':
            AC[i] = AC[i-1] + 1
        else:
            AC[i] = AC[i-1]
    for i in range(Q):
        l,r = map(int,input().split())
        print(AC[r-1]-AC[l-1])

=======
Suggestion 9

def main():
    n,q = map(int,input().split())
    s = input()
    ac = [0]*(n+1)

    for i in range(n):
        ac[i+1] = ac[i]
        if s[i:i+2] == "AC":
            ac[i+1] += 1

    for i in range(q):
        l,r = map(int,input().split())
        print(ac[r-1]-ac[l-1])

=======
Suggestion 10

def main():
    N,Q = map(int,input().split())
    S = input()
    #print(N,Q,S)
    l = []
    r = []
    for i in range(Q):
        l_i,r_i = map(int,input().split())
        l.append(l_i)
        r.append(r_i)
    #print(l)
    #print(r)

    #文字列のACの数をカウント
    #ACの数をカウントするためには、ACで始まる文字列の数とACで終わる文字列の数をそれぞれカウントすれば良い
    #ACで始まる文字列の数をカウントするためには、Sの先頭から2文字目以降でACが出現する回数をカウント
    #ACで終わる文字列の数をカウントするためには、Sの末尾から2文字目以前でACが出現する回数をカウント
    #ACで始まる文字列の数とACで終わる文字列の数をそれぞれカウントし、その積がACの数になる
    #ACで始まる文字列の数をカウントするためには、Sの先頭から2文字目以降でACが出現する回数をカウント
    #ACで終わる文字列の数をカウントするためには、Sの末尾から2文字目以前でACが出現する回数をカウント
    #ACで始まる文字列の数とACで終わる文字列の数をそれぞれカウントし、その積がACの数になる
    #ACで始まる文字列の数をカウントするためには、Sの先頭から2文字目以降でACが出現する回数をカウント
    #ACで終わる文字列の数をカウントするためには、Sの末尾から2文字目以前でACが出現する
