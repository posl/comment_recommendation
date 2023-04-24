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
    t = 0
    for i in range(N-1):
        t += A[i]
        if t > T:
            print('No')
            return
        for j in range(M):
            if X[j] == i+1:
                t += Y[j]
                if t > T:
                    print('No')
                    return
    print('Yes')

=======
Suggestion 2

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    time = 0
    for i in range(N-1):
        time += A[i]
        for j in range(M):
            if i+1 == X[j]:
                time += Y[j]
                break
        if time > T:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0 for i in range(M)]
    Y = [0 for i in range(M)]
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    time = 0
    for i in range(N-1):
        time += A[i]
        for j in range(M):
            if X[j] == i+1:
                time += Y[j]
        if time > T:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 4

def solve():
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
Suggestion 5

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for i in range(M):
        X, Y = map(int, input().split())
        B.append((X, Y))
    B.append((N, 0))
    B.sort()
    time = T
    for i in range(M+1):
        time -= A[B[i][0]-2]
        if time <= 0:
            print('No')
            return
        time += B[i][1]
        if time > T:
            time = T
    print('Yes')
    return

=======
Suggestion 6

def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i],Y[i] = map(int,input().split())
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        for j in range(M):
            if X[j] == i+1:
                t += Y[j]
                if t > T:
                    t = T
    print("Yes")
    return

=======
Suggestion 7

def main():
    N, M, T = map(int, raw_input().split())
    A = map(int, raw_input().split())
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, raw_input().split())
        X.append(x)
        Y.append(y)
    X.append(0)
    Y.append(0)
    X.append(N)
    Y.append(0)
    X.sort()
    Y.sort()
    X.reverse()
    Y.reverse()
    time = T
    for i in range(N):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        time += Y[X.index(i+1)]
    print("Yes")

=======
Suggestion 8

def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    bonus = []
    for i in range(M):
        bonus.append(list(map(int,input().split())))
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        if bonus and bonus[0][0] == i+1:
            t += bonus[0][1]
            bonus.pop(0)
    print("Yes")
    return

=======
Suggestion 9

def main():
    #Get input
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    
    #Initialize
    time = t
    room = 1
    
    #Move
    for i in range(n-1):
        time -= a[i]
        if time <= 0:
            print('No')
            return
        if (i+1) in x:
            time += y[x.index(i+1)]
        room += 1
    
    #Check if he can reach Room N
    if room == n:
        print('Yes')
    else:
        print('No')
    return

=======
Suggestion 10

def can_reach(N, M, T, A, X, Y):
    #Takahashi can reach Room N if he can reach Room N-1.  
    #If he can reach Room N-1, he can reach Room N-2, and so on.
    #If he can reach Room 1, he can reach Room 2, and so on.
    #So, we can solve this problem by dynamic programming.
    #Let dp[i] be True if he can reach Room i, and False otherwise.
    #dp[i] = True if dp[i-1] is True and T-A[i-1] >= 0, or dp[X[j]] is True and T-Y[j] >= 0 for some j.
    #If dp[N] is True, he can reach Room N.
    #If dp[N] is False, he cannot reach Room N.
    dp = [False] * (N+1)
    dp[1] = True
    for i in range(2, N+1):
        if dp[i-1] and T-A[i-2] >= 0:
            dp[i] = True
        for j in range(M):
            if dp[X[j]] and T-Y[j] >= 0:
                dp[i] = True
    return dp[N]
