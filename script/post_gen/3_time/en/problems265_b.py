Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    t = T
    for i in range(N - 1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        for j in range(M):
            if X[j] == i + 1:
                t += Y[j]
                if t > T:
                    t = T
    print("Yes")
    return

=======
Suggestion 2

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    ans = "Yes"
    t = T
    for i in range(N-1):
        t = t - A[i]
        if t <= 0:
            ans = "No"
            break
        for j in range(M):
            if X[j] == i+1:
                t = t + Y[j]
                if t > T:
                    t = T
    print(ans)

=======
Suggestion 3

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    time = 0
    bonus = 0
    for i in range(N-1):
        time += A[i]
        for j in range(M):
            if X[j] == i+1:
                bonus += Y[j]
        if time > T+bonus:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 4

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    X.append(N)
    Y.append(0)
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        j = 0
        while j < M+1 and X[j] < i+2:
            j += 1
        if j < M+1 and X[j] == i+2:
            t += Y[j]
    print("Yes")
    return

=======
Suggestion 5

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    #print(N, M, T, A, X, Y)

    #Takahashi starts with T seconds.
    #He can move from Room i to Room i+1 in A[i] seconds.
    #There are M bonus rooms.
    #When he reaches Room X[i], the time limit increases by Y[i] seconds.
    #Can he reach Room N?

    #We have to check whether he can reach Room N with time T.
    #If he can reach Room N with time T, then he can reach Room N with time T+Y[i] for any bonus room i.
    #So, we can check whether he can reach Room N with time T+Y[i] for any bonus room i.
    #We can check this by simulating the process.
    #We start with Room 1 and time T.
    #We move to Room 2 in A[0] seconds.
    #If the time is less than X[0], then we can move to Room 3 in A[1] seconds.
    #If the time is less than X[1], then we can move to Room 4 in A[2] seconds.
    #If the time is less than X[2], then we can move to Room 5 in A[3] seconds.
    #If the time is less than X[3], then we can move to Room 6 in A[4] seconds.
    #If the time is less than X[4], then we can move to Room 7 in A[5] seconds.
    #If the time is less than X[5], then we can move to Room 8 in A[6] seconds.
    #If the time is less than X[6], then we can move to Room 9 in A[7] seconds.
    #If the time is less than X[7], then we can move to Room 10 in A[8] seconds.
    #If the time is less than X[8], then we can move to Room 11 in A[9] seconds.

=======
Suggestion 6

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    time = T
    bonus = 0
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        if i+1 in X:
            time += Y[X.index(i+1)]
        if time > T:
            time = T
    print("Yes")
    return

=======
Suggestion 7

def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = [0] * m
    y = [0] * m
    for i in range(m):
        x[i], y[i] = map(int, input().split())
    time = t
    for i in range(n-1):
        time -= a[i]
        if time <= 0:
            print('No')
            return
        for j in range(m):
            if i+1 == x[j]:
                time += y[j]
                break
    print('Yes')

=======
Suggestion 8

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0 for i in range(M)]
    Y = [0 for i in range(M)]
    for i in range(M):
        X[i], Y[i] = map(int, input().split())

    time = T
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            return

        for j in range(M):
            if X[j] == i+1:
                time += Y[j]
                break

    print("Yes")

=======
Suggestion 9

def main():
    #input
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    B = []
    for i in range(M):
        X,Y = map(int,input().split())
        B.append([X,Y])
    #solve
    B.append([N,0])
    B.sort()
    time = T
    for i in range(M+1):
        time -= A[B[i][0]-2]
        if time <= 0:
            print("No")
            return
        time = min(T,time+B[i][1])
    print("Yes")
    return

=======
Suggestion 10

def main():
  N, M, T = map(int, input().split())
  A = list(map(int, input().split()))
  B = [0] * (N-1)
  for i in range(N-1):
    B[i] = T - A[i]
  for i in range(M):
    X, Y = map(int, input().split())
    B[X-1] += Y
  for i in range(N-1):
    if B[i] <= 0:
      print("No")
      return
  print("Yes")
  return
