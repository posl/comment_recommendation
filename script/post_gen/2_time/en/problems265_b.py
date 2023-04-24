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
    for i in range(N-1):
        T = T - A[i]
        if T <= 0:
            print("No")
            break
        else:
            if i+1 in X:
                T = T + Y[X.index(i+1)]
                if T >= 10**9:
                    T = 10**9
            if i == N-2:
                print("Yes")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    ans = 'Yes'
    time = 0
    max_time = T
    for i in range(N):
        if i == 0:
            time += A[i]
        elif i == N-1:
            time += A[i]
        else:
            time += A[i] - A[i-1]
        for j in range(M):
            if i == X[j]-1:
                time += Y[j]
        if time > max_time:
            ans = 'No'
            break
    print(ans)

=======
Suggestion 3

def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    Y = []
    for i in range(M):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    t = T
    p = 1
    for i in range(N-1):
        t = t - A[i]
        if t <= 0:
            print("No")
            return
        if p in X:
            t = min(T,t+Y[X.index(p)])
        p += 1
    print("Yes")
    return

=======
Suggestion 4

def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    Y = []
    for i in range(M):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    for i in range(N-1):
        T -= A[i]
        if T <= 0:
            print("No")
            return
        if i+1 in X:
            T += Y[X.index(i+1)]
            if T > M:
                T = M
    print("Yes")

=======
Suggestion 5

def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    Y = []
    for i in range(M):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    time = T
    room = 0
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print('No')
            break
        else:
            room += 1
            if room in X:
                time += Y[X.index(room)]
    if time > 0:
        print('Yes')

=======
Suggestion 6

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

    print("Yes")
    return

=======
Suggestion 7

def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    for i in range(n-1):
        t = t - a[i]
        if t <= 0:
            print('No')
            return
        if i+1 in x:
            t = min(t+y[x.index(i+1)],10**9)
    print('Yes')

=======
Suggestion 8

def problems265_b():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for i in range(m):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    t_ = t
    n_ = n
    for i in range(n-1):
        if t_ > 0:
            t_ -= a[i]
            if t_ > 0:
                n_ -= 1
                if n_ in x:
                    t_ += y[x.index(n_)]
            else:
                break
    if n_ == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    rooms = [list(map(int, input().split())) for i in range(m)]
    now = 0
    for i in range(n-1):
        t -= a[i] - now
        if t <= 0:
            print('No')
            return
        for room in rooms:
            if room[0] == i + 2:
                t += room[1]
                if t > 10**9:
                    t = 10**9
        now = a[i]
    t -= a[n-1] - now
    if t <= 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
