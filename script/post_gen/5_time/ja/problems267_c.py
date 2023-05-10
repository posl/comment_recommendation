Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - m + 1):
        tmp = 0
        for j in range(m):
            tmp += (j + 1) * a[i + j]
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    max_A = max(A)
    min_A = min(A)
    if M == 1:
        print(sum_A)
    elif max_A <= 0:
        print(max_A * M)
    elif min_A >= 0:
        print(sum_A + (M - 2) * min_A)
    else:
        A.sort(reverse=True)
        sum_A = 0
        for i in range(M):
            sum_A += A[i]
        print(sum_A + (M - 1) * min_A)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-m+1):
        tmp = 0
        for j in range(m):
            tmp += a[i+j]*(j+1)
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 4

def problem267_c():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    ans = -float("inf")
    for i in range(m,n+1):
        ans = max(ans,s[i]-s[i-m])
    print(ans)
problem267_c()

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i + 1]
    ans = 0
    for i in range(m):
        ans += a[i + 1] * (m - i)
    for i in range(n - m + 1):
        ans = max(ans, s[i + m] - s[i])
        for j in range(m):
            ans = max(ans, s[i + j] - s[i] + s[i + m] - s[i + j])
    print(ans)

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(1, N+1):
        if i == M:
            ans = max(ans, sum(A[:i]))
        elif i > M:
            ans = max(ans, sum(A[:i]) + sum(A[-(i-M):]))
    print(ans)

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    #print(A)
    #print(N,M)
    #print(A)
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A[61])
    #print(A[62])
    #print(A[63])
    #print(A[64])
    #print(A[65])

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = [0 for _ in range(N+1)]
    for i in range(N):
        B[i+1] = B[i] + A[i]
    import collections
    C = collections.deque()
    ans = 0
    for i in range(N+1):
        while C and B[C[-1]] >= B[i]:
            C.pop()
        C.append(i)
        if i >= M:
            if C[0] == i - M:
                C.popleft()
            ans = max(ans, B[i] - B[C[0]])
    print(ans)

=======
Suggestion 9

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    num = 0
    for i in range(m):
        num += a[i]
    for i in range(m,n):
        num += a[i] * (i+1)
    return num

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    t = [0] * (n + 1)
    for i in range(n):
        t[i + 1] = s[i + 1] - min(t[i], s[i + 1])
    print(max(t))
