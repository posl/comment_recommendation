Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    N, M, T = input().split()
    N = int(N)
    M = int(M)
    T = int(T)
    A = input().split()
    A = [int(i) for i in A]
    XY = []
    for i in range(M):
        XY.append(input().split())
        XY[i][0] = int(XY[i][0])
        XY[i][1] = int(XY[i][1])
    return N, M, T, A, XY

=======
Suggestion 2

def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for i in range(M)]

    time = T
    room = 1
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            exit()
        if room == XY[0][0]:
            time += XY[0][1]
            del XY[0]
        room += 1
    print("Yes")

=======
Suggestion 3

def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    XY.sort()
    X = [x for x, _ in XY]
    Y = [y for _, y in XY]
    if X[0] != 1:
        print("No")
        return
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        if i+1 in X:
            t += Y[X.index(i+1)]
            if t > T:
                t = T
    print("Yes")

=======
Suggestion 4

def isReachable(N,M,T,A,X,Y):
    #print(N,M,T,A,X,Y)
    #print("N = ",N)
    #print("M = ",M)
    #print("T = ",T)
    #print("A = ",A)
    #print("X = ",X)
    #print("Y = ",Y)
    #print()
    if N == 1:
        return True
    if N == 2:
        if M == 0:
            return True
        else:
            return False
    if N == 3:
        if T >= A[0] + A[1]:
            return True
        else:
            if M == 0:
                return False
            else:
                if T >= A[0] + Y[0]:
                    return True
                else:
                    return False
    if N == 4:
        if T >= A[0] + A[1] + A[2]:
            return True
        else:
            if M == 0:
                return False
            else:
                if T >= A[0] + A[1] + Y[0]:
                    return True
                else:
                    if T >= A[0] + Y[0] + Y[1]:
                        return True
                    else:
                        if T >= A[0] + Y[0] + A[2]:
                            return True
                        else:
                            return False
    if N == 5:
        if T >= A[0] + A[1] + A[2] + A[3]:
            return True
        else:
            if M == 0:
                return False
            else:
                if T >= A[0] + A[1] + A[2] + Y[0]:
                    return True
                else:
                    if T >= A[0] + A[1] + Y[0] + Y[1]:
                        return True
                    else:
                        if T >= A[0] + A[1] + Y[0] + A[3]:
                            return True
                        else:
                            if T >= A[0] + Y[0] + Y[1] + Y[2]:
                                return True
                            else:
                                if T >= A[0] + Y[0] + Y[1] + A[3]:
                                    return

=======
Suggestion 5

def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x1,y1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
    a.append(0)
    a.append(0)
    x.append(n)
    y.append(0)
    for i in range(m):
        a[x[i]-1] = a[x[i]-1] + y[i]
    for i in range(n-1):
        t = t - a[i]
        if t <= 0:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 6

def solve():
    N,M,T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    #print(N,M,T,A,XY)
    ans = 'No'
    time = T
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            break
        for xy in XY:
            if i+1 == xy[0]:
                time += xy[1]
        if i+1 == N-1 and time > 0:
            ans = 'Yes'
    print(ans)

=======
Suggestion 7

def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    now = 0
    for x, y in XY:
        if now + A[x - 1] >= T:
            print('No')
            return
        now += A[x - 1] + y
    if now + A[-1] >= T:
        print('No')
        return
    print('Yes')

=======
Suggestion 8

def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    
    X = [0]*(N+1)
    Y = [0]*(N+1)
    for x,y in XY:
        X[x] = x
        Y[x] = y
    
    t = T
    for i in range(1,N):
        t -= A[i-1]
        if t <= 0:
            print("No")
            return
        t = min(T,t+Y[i])
    print("Yes")

=======
Suggestion 9

def get_input():
    N,M,T = input().split()
    N = int(N)
    M = int(M)
    T = int(T)
    A = input().split()
    A = [int(a) for a in A]
    XY = []
    for i in range(M):
        x,y = input().split()
        x = int(x)
        y = int(y)
        XY.append((x,y))
    return N, M, T, A, XY

=======
Suggestion 10

def solve():
    N,M,T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    XY.sort()
    i = 0
    for x,y in XY:
        while i < N-1 and i+1 < x:
            T -= A[i]
            if T <= 0:
                print("No")
                return
            i += 1
        T += y
        if T > A[i]:
            T = A[i]
        i += 1
    while i < N-1:
        T -= A[i]
        if T <= 0:
            print("No")
            return
        i += 1
    print("Yes")
