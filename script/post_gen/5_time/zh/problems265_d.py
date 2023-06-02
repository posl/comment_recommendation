Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * 4 for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = max(dp[i-1][0], p*a[i-1])
        dp[i][1] = max(dp[i-1][1], dp[i][0] + q*a[i-1])
        dp[i][2] = max(dp[i-1][2], dp[i][1] + r*a[i-1])
    print(dp[n][2])

=======
Suggestion 2

def get_input():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    return N, P, Q, R, A

=======
Suggestion 3

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, P, Q, R)
    # print(A)
    # print(sum(A))
    # print(P+Q+R)
    if N == 3:
        if P+Q+R == sum(A):
            print('Yes')
        else:
            print('No')
    else:
        # print('No')
        # print(N, P, Q, R)
        # print(A)
        # print(sum(A))
        # print(P+Q+R)
        for i in range(N-3+1):
            for j in range(i+1, N-2+1):
                for k in range(j+1, N-1+1):
                    for l in range(k+1, N+1):
                        # print(i, j, k, l)
                        if sum(A[i:j]) == P and sum(A[j:k]) == Q and sum(A[k:l]) == R:
                            print('Yes')
                            return
        print('No')

=======
Suggestion 4

def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,p,q,r)
    #print(a)
    #print(len(a))
    #print(a[0])
    #print(a[1])
    #print(a[2])
    #print(a[3])
    #print(a[4])
    #print(a[5])
    #print(a[6])
    #print(a[7])
    #print(a[8])
    #print(a[9])
    #print(a[10])
    #print(a[11])
    #print(a[12])
    #print(a[13])
    #print(a[14])
    #print(a[15])
    #print(a[16])
    #print(a[17])
    #print(a[18])
    #print(a[19])
    #print(a[20])
    #print(a[21])
    #print(a[22])
    #print(a[23])
    #print(a[24])
    #print(a[25])
    #print(a[26])
    #print(a[27])
    #print(a[28])
    #print(a[29])
    #print(a[30])
    #print(a[31])
    #print(a[32])
    #print(a[33])
    #print(a[34])
    #print(a[35])
    #print(a[36])
    #print(a[37])
    #print(a[38])
    #print(a[39])
    #print(a[40])
    #print(a[41])
    #print(a[42])
    #print(a[43])
    #print(a[44])
    #print(a[45])
    #print(a[46])
    #print(a[47])
    #print(a[48])
    #print(a[49])
    #print(a[50])
    #print(a[51])
    #print(a[52])
    #print(a[53])
    #print(a[54])
    #print(a[55])
    #print(a[56])
    #print(a[57])
    #print(a[58])
    #print(a[59])
    #print(a[60])
    #print(a[61])
    #print(a[62])
    #print(a[63])
    #print(a[64])
    #

=======
Suggestion 5

def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    max_a = max(a)
    min_a = min(a)
    if max_a == min_a:
        if p == max_a and q == max_a and r == max_a:
            print('Yes')
        else:
            print('No')
        return
    if p == min_a:
        start = a.index(min_a)
    elif q == min_a:
        start = a.index(min_a) + 1
    elif r == min_a:
        start = a.index(min_a) + 2
    else:
        print('No')
        return
    if start + 2 >= n:
        print('No')
        return
    if p == min_a:
        if p == q:
            if p == r:
                print('Yes')
                return
            else:
                if a[start + 2] == r:
                    print('Yes')
                    return
                else:
                    print('No')
                    return
        else:
            if a[start + 1] == q and a[start + 2] == r:
                print('Yes')
                return
            else:
                print('No')
                return
    elif q == min_a:
        if q == r:
            if q == p:
                print('Yes')
                return
            else:
                if a[start + 2] == p:
                    print('Yes')
                    return
                else:
                    print('No')
                    return
        else:
            if a[start + 1] == r and a[start + 2] == p:
                print('Yes')
                return
            else:
                print('No')
                return
    elif r == min_a:
        if r == p:
            if r == q:
                print('Yes')
                return
            else:
                if a[start + 2] == q:
                    print('Yes')
                    return
                else:
                    print('No')
                    return
        else:
            if a[start + 1] == p and a[start + 2] == q:
                print('Yes')
                return
            else:
                print('No')
                return
    else:
        print('No')
        return

=======
Suggestion 6

def solve():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    m1 = [0] * (n + 1)
    m2 = [0] * (n + 1)
    m3 = [0] * (n + 1)
    for i in range(1, n + 1):
        m1[i] = max(m1[i - 1], s[i] - p)
        m2[i] = max(m2[i - 1], s[i] - q)
        m3[i] = max(m3[i - 1], s[i] - r)
    ans = 0
    for i in range(n + 1):
        ans = max(ans, m1[i] + m2[i] + m3[i])
    print(ans)


solve()

=======
Suggestion 7

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    P -= 1
    Q -= 1
    R -= 1
    A.sort()
    ans = 0
    for i in range(N):
        if i > 0 and A[i] == A[i - 1]:
            continue
        if A[i] > R:
            break
        x = i
        y = -1
        z = -1
        for j in range(i + 1, N):
            if j > i + 1 and A[j] == A[j - 1]:
                continue
            if A[j] > Q:
                break
            if A[j] == A[i]:
                y = j
            else:
                z = j
        if y == -1 or z == -1:
            continue
        for j in range(z + 1, N):
            if j > z + 1 and A[j] == A[j - 1]:
                continue
            if A[j] > P:
                break
            if A[j] == A[z]:
                ans += 1
                break
    if ans > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n,p,q,r=map(int,input().split())
    a=list(map(int,input().split()))
    b=[a[0]]
    for i in range(1,n):
        b.append(b[i-1]+a[i])
    c=[b[0]]
    for i in range(1,n):
        c.append(c[i-1]+b[i])
    d=[c[0]]
    for i in range(1,n):
        d.append(d[i-1]+c[i])
    e=[d[0]]
    for i in range(1,n):
        e.append(e[i-1]+d[i])
    f=[e[0]]
    for i in range(1,n):
        f.append(f[i-1]+e[i])
    g=[f[0]]
    for i in range(1,n):
        g.append(g[i-1]+f[i])
    h=[g[0]]
    for i in range(1,n):
        h.append(h[i-1]+g[i])
    i=[h[0]]
    for i in range(1,n):
        i.append(i[i-1]+h[i])
    j=[i[0]]
    for i in range(1,n):
        j.append(j[i-1]+i[i])
    k=[j[0]]
    for i in range(1,n):
        k.append(k[i-1]+j[i])
    l=[k[0]]
    for i in range(1,n):
        l.append(l[i-1]+k[i])
    m=[l[0]]
    for i in range(1,n):
        m.append(m[i-1]+l[i])
    n=[m[0]]
    for i in range(1,n):
        n.append(n[i-1]+m[i])
    o=[n[0]]
    for i in range(1,n):
        o.append(o[i-1]+n[i])
    p=[o[0]]
    for i in range(1,n):
        p.append(p[i-1]+o[i])
    q=[p[0]]
    for i in range(1,n):
        q.append(q[i-1]+p[i])
    r=[q[0]]
    for i in range(1,n):
        r.append(r[i-1]+q[i])
    s=[r[0]]
    for i in range(1,n):
        s

=======
Suggestion 9

def solve():
    n,p,q,r=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    #print(a)
    #print(n,p,q,r)
    #print(a[0],a[1])
    #print(a[1],a[2])
    #print(a[2],a[3])
    #print(a[3],a[4])
    #print(a[4],a[5])
    #print(a[5],a[6])
    #print(a[6],a[7])
    #print(a[7],a[8])
    #print(a[8],a[9])
    #print(a[9],a[10])
    #print(a[10],a[11])
    #print(a[11],a[12])
    #print(a[12],a[13])
    #print(a[13],a[14])
    #print(a[14],a[15])
    #print(a[15],a[16])
    #print(a[16],a[17])
    #print(a[17],a[18])
    #print(a[18],a[19])
    #print(a[19],a[20])
    #print(a[20],a[21])
    #print(a[21],a[22])
    #print(a[22],a[23])
    #print(a[23],a[24])
    #print(a[24],a[25])
    #print(a[25],a[26])
    #print(a[26],a[27])
    #print(a[27],a[28])
    #print(a[28],a[29])
    #print(a[29],a[30])
    #print(a[30],a[31])
    #print(a[31],a[32])
    #print(a[32],a[33])
    #print(a[33],a[34])
    #print(a[34],a[35])
    #print(a[35],a[36])
    #print(a[36],a[37])
    #print(a[37],a[38])
    #print(a[38],a[39])
    #print(a[39],a[40])
    #print(a[40],a[41])
    #print(a[41],a[

=======
Suggestion 10

def solve():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    min_a = [a[0]]
    max_a = [a[0]]
    for i in range(1, n):
        min_a.append(min(min_a[i - 1], a[i]))
        max_a.append(max(max_a[i - 1], a[i]))
    ans = 0
    for i in range(n):
        if min_a[i] >= p and max_a[i] <= r:
            ans += 1
    print(ans)
