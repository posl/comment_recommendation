Synthesizing 10/10 solutions

=======
Suggestion 1

def getMedian(arr):
    arr.sort()
    l = len(arr)
    if l%2 == 0:
        return arr[l/2-1]
    else:
        return arr[(l+1)/2-1]

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    A = []
    for i in range(N):
        A.append(list(map(int,input().split())))
    print(A)

=======
Suggestion 3

def get_median(a):
    a.sort()
    return a[len(a) // 2]

=======
Suggestion 4

def get_median(a):
    a.sort()
    l = len(a)
    if l%2 == 1:
        return a[(l-1)//2]
    else:
        return a[l//2-1]

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans = 10**9
    for i in range(n-k+1):
        for j in range(n-k+1):
            b = []
            for p in range(k):
                for q in range(k):
                    b.append(a[i+p][j+q])
            b.sort()
            ans = min(ans,b[k*k//2])
    print(ans)

=======
Suggestion 6

def get_median(a, k):
    a.sort()
    return a[k*k//2]

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def getMedian(a, k):
    n = len(a)
    b = []
    for i in range(n-k+1):
        for j in range(n-k+1):
            c = []
            for x in range(k):
                for y in range(k):
                    c.append(a[i+x][j+y])
            c.sort()
            b.append(c[(k*k)//2])
    b.sort()
    return b[0]

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    #a = [[1,7,0],[5,8,11],[10,4,2]]
    #a = [[1,2,3],[4,5,6],[7,8,9]]
    #print(a)
    ans = 10**9
    for i in range(n-k+1):
        for j in range(n-k+1):
            #print(i,j)
            b = []
            for x in range(i,i+k):
                for y in range(j,j+k):
                    b.append(a[x][y])
            b.sort()
            #print(b)
            ans = min(ans,b[(k**2)//2])
    print(ans)

=======
Suggestion 10

def get_median(arr):
    arr.sort()
    if len(arr)%2==0:
        return (arr[len(arr)//2]+arr[len(arr)//2-1])/2
    else:
        return arr[len(arr)//2]

n,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
ans=10**9
for i in range(n-k+1):
    for j in range(n-k+1):
        arr=[]
        for x in range(k):
            for y in range(k):
                arr.append(a[i+x][j+y])
        ans=min(ans,get_median(arr))
print(int(ans))
