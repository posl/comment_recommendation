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
    return

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
        time = time - A[i]
        if time <= 0:
            print("No")
            return
        if room in X:
            time = time + Y[X.index(room)]
        room = room + 1

    print("Yes")

=======
Suggestion 3

def main():
    N,M,T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x,y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    for i in range(M):
        if i == 0:
            if T - A[X[i]-1] + Y[i] > 0:
                T = T - A[X[i]-1] + Y[i]
            else:
                print("No")
                return
        else:
            if T - A[X[i]-X[i-1]-1] + Y[i] - A[X[i-1]-1] > 0:
                T = T - A[X[i]-X[i-1]-1] + Y[i] - A[X[i-1]-1]
            else:
                print("No")
                return
    
    if T - A[N-1-X[M-1]-1] > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def problems265_b():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = [0] * m
    y = [0] * m
    for i in range(m):
        x[i], y[i] = map(int, input().split())
    for i in range(n-1):
        t = t - a[i]
        if t <= 0:
            print("No")
            return
        for j in range(m):
            if x[j] == i+1:
                t = t + y[j]
                if t > 0:
                    break
    t = t - a[n-1]
    if t > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(M):
        X, Y = map(int, input().split())
        A[X-1] = Y
    time = T
    for i in range(N-1):
        time = time - A[i]
        if time <= 0:
            print('No')
            exit()
        time = min(time+A[i+1]-A[i], T)
    time = time - A[N-1]
    if time <= 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 6

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    B = [list(map(int, input().split())) for i in range(M)]
    flag = True
    time = T
    for i in range(0, N-1):
        if time <= 0:
            flag = False
            break
        time -= A[i]
        if time > 0:
            time += B[i][1]
        else:
            time = B[i][1]
        if time > T:
            time = T
    if flag:
        if time > 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 7

def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    bonus = []
    for _ in range(m):
        bonus.append(list(map(int,input().split())))
    now = 0
    for i in range(n):
        now += a[i]
        if now > t:
            print('No')
            return
        for j in range(m):
            if i+1 == bonus[j][0]:
                now += bonus[j][1]
                if now > t:
                    print('No')
                    return
    print('Yes')
    return

=======
Suggestion 8

def problem265_b():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(m)]
    current_time = t
    current_room = 1

    for i in range(m):
        current_time = current_time - (xy[i][0] - current_room)
        current_room = xy[i][0]
        if current_time <= 0:
            print("No")
            return

        current_time = current_time + xy[i][1]
        if current_time > t:
            current_time = t

    current_time = current_time - (n - current_room)
    if current_time <= 0:
        print("No")
        return

    print("Yes")

=======
Suggestion 9

def read_ints():
    return list(map(int, input().split()))

N,M,T = read_ints()
A = read_ints()
XY = [read_ints() for _ in range(M)]

time = T
prev = 0
for i in range(N-1):
    time = time - (A[i] - prev)
    prev = A[i]
    if time <= 0:
        print("No")
        exit()
    for j in range(M):
        if i+1 == XY[j][0]:
            time = time + XY[j][1]
            break
print("Yes")

=======
Suggestion 10

def bonus_rooms(n,m,t,a,x,y):
  time_limit = t
  current_room = 1
  for i in range(n-1):
    time_limit -= a[i]
    if time_limit <= 0:
      return False
    if current_room in x:
      time_limit = min(t, time_limit + y[x.index(current_room)])
    current_room += 1
  return True

n,m,t = map(int, input().split())
a = list(map(int, input().split()))
x = []
y = []
for i in range(m):
  x_i, y_i = map(int, input().split())
  x.append(x_i)
  y.append(y_i)
