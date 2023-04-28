Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    t = T
    p = 0
    for i in range(N-1):
        t = t - A[i] + (X[p] - i - 1) * Y[p]
        if t <= 0:
            break
        if i+1 == X[p]:
            t += Y[p]
            p += 1
            if p == M:
                break

    if t > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    time = T
    room = 1
    for i in range(N - 1):
        time += Y[i] - (X[i] - room)
        if time <= 0:
            print("No")
            return
        room = X[i]
        time -= A[i]
        if time <= 0:
            print("No")
            return
    
    time += Y[N - 1] - (N - room)
    if time <= 0:
        print("No")
        return
    print("Yes")
    return

=======
Suggestion 3

def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for i in range(m):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    time = t
    room = 1
    for i in range(n-1):
        time -= a[i]
        if time <= 0:
            print("No")
            return
        if room in x:
            time += y[x.index(room)]
        room += 1
    if time <= 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i],Y[i] = map(int,input().split())
    time = T
    room = 1
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            return False
        if room in X:
            time += Y[X.index(room)]
            if time > T:
                time = T
        room += 1
    return True if time - A[N-2] > 0 else False

print('Yes' if solve() else 'No')

=======
Suggestion 5

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        X_i, Y_i = map(int, input().split())
        X.append(X_i)
        Y.append(Y_i)
    time = T
    room = 1
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            exit()
        if room in X:
            time += Y[X.index(room)]
        room += 1
    print("Yes")

=======
Suggestion 6

def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for _ in range(m):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)

    time = 0
    prev = 0
    for i in range(n):
        if i == 0:
            time = t
        else:
            time -= (a[i-1]-a[i-2])
        if time <= 0:
            print('No')
            return
        if i+1 in x:
            time += (y[x.index(i+1)] - prev)
            prev = y[x.index(i+1)]
        else:
            if prev != 0:
                time += (y[x.index(i+1)] - prev)
                prev = y[x.index(i+1)]
    if time - (a[-1]-a[-2]) <= 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    current_time = T
    current_room = 1
    for i in range(N-1):
        current_time -= A[i]
        if current_time <= 0:
            print("No")
            return
        for x, y in XY:
            if current_room == x:
                current_time = min(T, current_time + y)
        current_room += 1
    print("Yes" if current_time - A[-1] > 0 else "No")

=======
Suggestion 8

def problems265_b():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for i in range(m):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    time = 0
    for i in range(n-1):
        time += a[i]
        if time >= t:
            print('No')
            return
        if i+1 in x:
            time = min(time + y[x.index(i+1)], t)
    print('Yes')
    return

=======
Suggestion 9

def problem265_b():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    for i in range(m):
        t = t - (x[i] - x[i-1]) - a[x[i]-2] + y[i]
        if t <= 0:
            print("No")
            exit()
    t = t - (n - x[m-1]) - a[n-2]
    if t <= 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def solve():
    N,M,T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = []
    for i in range(M):
        XY.append(list(map(int, input().split())))
    #print(N,M,T,A,XY)

    currentRoom = 1
    currentTime = T
    for i in range(N-1):
        #print("currentRoom: ", currentRoom, "currentTime: ", currentTime)
        if A[i] < currentTime:
            currentTime = currentTime - A[i]
            currentRoom = currentRoom + 1
            #print("currentRoom: ", currentRoom, "currentTime: ", currentTime)
        else:
            break

    #print("currentRoom: ", currentRoom, "currentTime: ", currentTime)
    #print("-----")
    if currentRoom == N:
        print("Yes")
        return

    for i in range(M):
        #print("currentRoom: ", currentRoom, "currentTime: ", currentTime)
        if XY[i][0] < currentRoom:
            continue
        else:
            currentTime = currentTime + XY[i][1]
            currentRoom = XY[i][0]
            #print("currentRoom: ", currentRoom, "currentTime: ", currentTime)
            if currentRoom == N:
                if currentTime > T:
                    print("No")
                    return
                else:
                    print("Yes")
                    return

    print("No")
    return
