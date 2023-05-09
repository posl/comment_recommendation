Synthesizing 10/10 solutions

=======
Suggestion 1

def get_distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]

distances = []
for i in range(n):
    for j in range(i + 1, n):
        distances.append(get_distance(xy[i][0], xy[i][1], xy[j][0], xy[j][1]))

distances.sort()
distances.reverse()
answer = 0
for i in range(k - 1):
    answer += distances[i]
print(answer)

=======
Suggestion 2

def get_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    #print(N, K, A, XY)
    print(solve(N, K, A, XY))

=======
Suggestion 4

def distance(x1,y1,x2,y2):
    return (((x1-x2)**2)+((y1-y2)**2))**0.5

N, K = map(int, input().split())
A = list(map(int, input().split()))
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(N)]
    
    #print(N, K)
    #print(A

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(N)]
    print(solve(N,K,A,XY))

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(N)]

    def check(r):
        for i in range(N):
            x, y = XY[i]
            for j in range(i+1, N):
                x2, y2 = XY[j]
                if (x2-x)**2 + (y2-y)**2 <= r**2:
                    break
            else:
                return False
        return True

    l = 0
    r = 10**9
    while r - l > 1e-5:
        m = (l+r)/2
        if check(m):
            r = m
        else:
            l = m
    print(r)

=======
Suggestion 8

def distance(x1,y1,x2,y2):
    return (abs(x1-x2)**2+abs(y1-y2)**2)**(1/2)

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    A = sorted(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(N)]
    X = [x for x,y in XY]
    Y = [y for x,y in XY]
    ans = 10**10
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                a = A.index(i+1)
                b = A.index(j+1)
                c = A.index(k+1)
                x1 = max(X[a],X[b],X[c])
                x2 = min(X[a],X[b],X[c])
                y1 = max(Y[a],Y[b],Y[c])
                y2 = min(Y[a],Y[b],Y[c])
                ans = min(ans,(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    print(ans**0.5)

=======
Suggestion 10

def solve():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(N)]

    ans = 10**20
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if i+1 in A and j+1 in A and k+1 in A:
                    x1,y1 = XY[i]
                    x2,y2 = XY[j]
                    x3,y3 = XY[k]
                    a = (x1-x2)**2 + (y1-y2)**2
                    b = (x2-x3)**2 + (y2-y3)**2
                    c = (x3-x1)**2 + (y3-y1)**2
                    ans = min(ans, max(a,b,c)**0.5)

    print(ans)
