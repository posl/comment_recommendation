Synthesizing 10/10 solutions

=======
Suggestion 1

def findMedian(arr):
    if len(arr) == 0:
        return 0
    arr.sort()
    if len(arr) % 2 == 0:
        return arr[len(arr) // 2]
    else:
        return arr[(len(arr) - 1) // 2]

=======
Suggestion 2

def solution():
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    m = k*k//2+1
    ans = 10**9
    for i in range(n-k+1):
        for j in range(n-k+1):
            b = []
            for p in range(k):
                for q in range(k):
                    b.append(a[i+p][j+q])
            b.sort()
            ans = min(ans, b[m-1])
    print(ans)

=======
Suggestion 3

def find_median(array):
    array.sort()
    return array[(len(array)-1)//2]

=======
Suggestion 4

def get_median(x,y):
    return (x+y+1)//2

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = float('inf')
    for i in range(n-k+1):
        for j in range(n-k+1):
            b = []
            for x in range(i, i+k):
                for y in range(j, j+k):
                    b.append(a[x][y])
            b.sort()
            ans = min(ans, b[k*k//2])
    print(ans)

=======
Suggestion 6

def median(m, n, k, arr):
    #print(m, n, k, arr)
    s = []
    for i in range(m-k+1):
        for j in range(n-k+1):
            #print(i, j)
            t = []
            for x in range(k):
                for y in range(k):
                    t.append(arr[i+x][j+y])
            t.sort()
            #print(t)
            s.append(t[(k*k//2)+1])
    s.sort()
    #print(s)
    return s[0]

=======
Suggestion 7

def get_median(arr):
    arr.sort()
    return arr[(len(arr)-1)//2]

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans = 10**9+1
    for i in range(n-k+1):
        for j in range(n-k+1):
            b = []
            for l in range(k):
                for m in range(k):
                    b.append(a[i+l][j+m])
            b.sort()
            ans = min(ans,b[k**2//2])
    print(ans)

=======
Suggestion 9

def getMedian(a):
    #a.sort()
    #print(a)
    #return a[int(len(a)/2)]
    return sorted(a)[int(len(a)/2)]

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    def check(x):
        B = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N):
            for j in range(N):
                B[i + 1][j + 1] = B[i + 1][j] + B[i][j + 1] - B[i][j]
                if A[i][j] > x:
                    B[i + 1][j + 1] += 1
        for i in range(N - K + 1):
            for j in range(N - K + 1):
                if B[i + K][j + K] - B[i][j + K] - B[i + K][j] + B[i][j] <= (K * K) // 2:
                    return True
        return False

    lb = -1
    ub = 10 ** 9 + 1
    while ub - lb > 1:
        mid = (lb + ub) // 2
        if check(mid):
            ub = mid
        else:
            lb = mid
    print(ub)
