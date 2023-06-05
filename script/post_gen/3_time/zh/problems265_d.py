Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, P, Q, R)
    #print(A)
    dp = [[0 for _ in range(3)] for _ in range(N)]
    dp[0][0] = P * A[0]
    dp[0][1] = dp[0][0] + Q * A[0]
    dp[0][2] = dp[0][1] + R * A[0]
    for i in range(1, N):
        dp[i][0] = max(dp[i-1][0], P * A[i])
        dp[i][1] = max(dp[i-1][1], dp[i][0] + Q * A[i])
        dp[i][2] = max(dp[i-1][2], dp[i][1] + R * A[i])
    print(dp[N-1][2])
    return

solve()

=======
Suggestion 2

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    maxA = [0] * N
    minA = [0] * N
    maxA[0] = A[0]
    minA[0] = A[0]
    for i in range(1, N):
        maxA[i] = max(maxA[i - 1], A[i])
        minA[i] = min(minA[i - 1], A[i])
    res = 0
    for i in range(N):
        if minA[i] < P:
            continue
        if maxA[i] > R:
            continue
        if maxA[i] - minA[i] > R - P:
            continue
        if minA[i] == P and maxA[i] == R:
            res += 1
            continue
        if minA[i] == P:
            if maxA[i] == Q:
                res += 1
            continue
        if maxA[i] == R:
            if minA[i] == Q:
                res += 1
            continue
        if minA[i] == Q:
            if maxA[i] == R:
                res += 1
            continue
        if maxA[i] - minA[i] == Q - P:
            res += 1
    if res == 0:
        print('No')
    else:
        print('Yes')
solve()

=======
Suggestion 3

def is_ok(a,b,c,d):
    if a < b < c < d:
        return True
    else:
        return False

n,p,q,r = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a)
for i in range(n-3):
    if is_ok(i,i+1,i+2,i+3):
        if a[i]+a[i+1]+a[i+2] == p and a[i+1]+a[i+2] == q and a[i+2] == r:
            print("Yes")
            exit()
print("No")

=======
Suggestion 4

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, P, Q, R)
    # print(A)
    # print(sum(A))
    # print(P+Q+R)
    if sum(A) == P+Q+R:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(N, P, Q, R)
    for i in range(N):
        if A[i] > R:
            break
        for j in range(i+1, N):
            if A[j] > R:
                break
            for k in range(j+1, N):
                if A[k] > R:
                    break
                for l in range(k+1, N):
                    if A[l] > R:
                        break
                    if (A[i] + A[i+1] + A[j] + A[j+1] + A[k] + A[k+1] + A[l] + A[l+1]) == (P + Q + R):
                        print("Yes")
                        return
    print("No")

=======
Suggestion 6

def main():
    n, p, q, r = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = [0] * n
    c = [0] * n
    d = [0] * n
    b[0] = a[0]
    c[0] = a[0] + a[1]
    d[0] = a[0] + a[1] + a[2]
    for i in range(1, n):
        b[i] = max(a[i], b[i - 1])
        c[i] = max(b[i - 1] + a[i], c[i - 1])
        d[i] = max(c[i - 1] + a[i], d[i - 1])
    ans = 0
    for i in range(n):
        ans = max(ans, p * b[i] + q * c[i] + r * d[i])
    print(ans)

=======
Suggestion 7

def solve():
    n,p,q,r = map(int, input().split())
    a = list(map(int, input().split()))
    max_a = max(a)
    min_a = min(a)
    if max_a == min_a:
        print('Yes')
        return
    if p == q == r:
        print('Yes')
        return
    if max_a == p and max_a == q and max_a == r:
        print('Yes')
        return
    if max_a == p and max_a == q and min_a == r:
        print('Yes')
        return
    if max_a == p and min_a == q and max_a == r:
        print('Yes')
        return
    if min_a == p and max_a == q and max_a == r:
        print('Yes')
        return
    if max_a == p and min_a == q and min_a == r:
        print('Yes')
        return
    if min_a == p and max_a == q and min_a == r:
        print('Yes')
        return
    if min_a == p and min_a == q and max_a == r:
        print('Yes')
        return
    if min_a == p and min_a == q and min_a == r:
        print('Yes')
        return
    print('No')
    return

=======
Suggestion 8

def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    s = [0]
    for i in range(n):
        s.append(s[i]+a[i])
    #print(s)
    ans = 0
    for i in range(n-1):
        if a[i] > q:
            break
        for j in range(i+1,n):
            if a[j] > r:
                break
            ans = max(ans,p*a[i]+q*(a[j]-a[i])+r*(s[n]-s[j]))
    print(ans)

=======
Suggestion 9

def main():
    n,p,q,r=map(int,input().split())
    a=list(map(int,input().split()))
    maxa=[0]*n
    maxa[-1]=a[-1]
    for i in range(n-2,-1,-1):
        maxa[i]=max(maxa[i+1],a[i])
    mina=[0]*n
    mina[-1]=a[-1]
    for i in range(n-2,-1,-1):
        mina[i]=min(mina[i+1],a[i])
    for i in range(n):
        if mina[i]<=p and maxa[i]>=p and mina[i]<=q-p and maxa[i]>=q-p and mina[i]<=r-q+p and maxa[i]>=r-q+p:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, P, Q, R)
    # print(A)
    # print('------')
    # print(len(A))
    # print(A[1:3])
    # print(A[2:4])
    # print(A[3:5])
    # print(A[4:6])
    # print(A[5:7])
    # print(A[6:8])
    # print(A[7:9])
    # print(A[8:10])
    # print(A[9:11])
    # print(A[10:12])
    # print(A[11:13])
    # print(A[12:14])
    # print(A[13:15])
    # print(A[14:16])
    # print(A[15:17])
    # print(A[16:18])
    # print(A[17:19])
    # print(A[18:20])
    # print(A[19:21])
    # print(A[20:22])
    # print(A[21:23])
    # print(A[22:24])
    # print(A[23:25])
    # print(A[24:26])
    # print(A[25:27])
    # print(A[26:28])
    # print(A[27:29])
    # print(A[28:30])
    # print(A[29:31])
    # print(A[30:32])
    # print(A[31:33])
    # print(A[32:34])
    # print(A[33:35])
    # print(A[34:36])
    # print(A[35:37])
    # print(A[36:38])
    # print(A[37:39])
    # print(A[38:40])
    # print(A[39:41])
    # print(A[40:42])
    # print(A[41:43])
    # print(A[42:44])
    # print(A[43:45])
    # print(A[44:46])
    # print(A[45:47])
    # print(A[46:48])
    # print(A[47:49])
    # print(A[48:50])
    # print(A[49:51])
    #
