Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)

    max = 0
    for i in range(N):
        if i == 0:
            max += A[i]
            continue
        t = T[i] - T[i-1]
        x = abs(X[i] - X[i-1])
        if t < x:
            continue
        elif t == x:
            max += A[i]
        else:
            max += A[i] - (t - x)
    print(max)

=======
Suggestion 2

def solve():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())

    max_sum = 0
    for i in range(N):
        if i == 0:
            max_sum = A[i]
            continue
        if T[i] - T[i-1] >= abs(X[i] - X[i-1]):
            max_sum += A[i]
    print(max_sum)

=======
Suggestion 3

def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append([t, x, a])

    #print(snuke)

    #snuke.sort(key=lambda x: x[0])
    #print(snuke)

    #snuke.sort(key=lambda x: x[1])
    #print(snuke)

    #snuke.sort(key=lambda x: x[2])
    #print(snuke)

    time = 0
    sum = 0
    for i in range(n):
        if snuke[i][0] >= snuke[i][1] + time:
            sum = sum + snuke[i][2]
            time = snuke[i][0]
            #print("sum = ", sum)
            #print("time = ", time)

    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t,x,a = map(int,input().split())
        snuke.append((t,x,a))
    snuke.append((0,0,0))
    snuke.append((10**5,0,0))
    snuke.sort()
    dp = [0]*(n+2)
    for i in range(1,n+2):
        dp[i] = max(dp[i-1],dp[i])
        if snuke[i-1][1] == snuke[i][1]:
            dp[i] = max(dp[i],dp[i-1]+snuke[i][2])
        else:
            dp[i] = max(dp[i],dp[i-1]+snuke[i][2]-abs(snuke[i][1]-snuke[i-1][1]))
    print(dp[n+1])

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    for i in range(n):
        t, x, a = map(int, input().split())
        s.append([t, x, a])
    s.append([float('inf'), 0, 0])
    s.sort()
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i], dp[i + 1])
        for j in range(i + 1, n + 1):
            if s[j][0] - s[i][0] >= abs(s[j][1] - s[i][1]):
                dp[j] = max(dp[j], dp[i] + s[j][2])
    print(dp[n])

=======
Suggestion 6

def solve():
    N = int(input())
    snukes = []
    for i in range(N):
        t, x, a = map(int, input().split())
        snukes.append((t, x, a))
    #print(snukes)
    snukes.sort()
    #print(snukes)
    #print(snukes[-1])
    max_size = 0
    for i in range(N):
        t, x, a = snukes[i]
        #print("t, x, a:", t, x, a)
        if t > x:
            continue
        elif t == x:
            max_size += a
        else:
            max_size += a
            for j in range(i+1, N):
                t, x, a = snukes[j]
                #print("t, x, a:", t, x, a)
                if t > x:
                    continue
                elif t == x:
                    max_size += a
                else:
                    break
            break
    print(max_size)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    for i in range(n):
        t, x, a_ = map(int, input().split())
        a.append((t, x, a_))
    a.sort()
    dp = [0] * 5
    for t, x, a_ in a:
        if x == 0:
            dp[0] = max(dp[0], dp[0] + a_)
        elif x == 1:
            dp[1] = max(dp[1], dp[0] + a_)
            dp[0] = max(dp[0], dp[0] + a_)
        elif x == 2:
            dp[2] = max(dp[2], dp[1] + a_)
            dp[1] = max(dp[1], dp[0] + a_)
            dp[0] = max(dp[0], dp[0] + a_)
        elif x == 3:
            dp[3] = max(dp[3], dp[2] + a_)
            dp[2] = max(dp[2], dp[1] + a_)
            dp[1] = max(dp[1], dp[0] + a_)
            dp[0] = max(dp[0], dp[0] + a_)
        else:
            dp[4] = max(dp[4], dp[3] + a_)
            dp[3] = max(dp[3], dp[2] + a_)
            dp[2] = max(dp[2], dp[1] + a_)
            dp[1] = max(dp[1], dp[0] + a_)
            dp[0] = max(dp[0], dp[0] + a_)
    print(max(dp))

=======
Suggestion 8

def solve():
    N, *T = map(int, open(0).read().split())
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = T[i * 3], T[i * 3 + 1], T[i * 3 + 2]
    ans = 0
    for i in range(N):
        if T[i] <= X[i]:
            ans += A[i]
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    #print(N, S)
    #dp = [[0 for _ in range(5)] for _ in range(N+1)]
    dp = [[0 for _ in range(5)] for _ in range(N)]
    #print(dp)
    for i in range(N):
        for j in range(5):
            if j == S[i][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + S[i][2])
            elif j >= 1 and dp[i-1][j-1] > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + S[i][2])
            elif j <= 3 and dp[i-1][j+1] > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j+1] + S[i][2])
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
    #print(dp)
    print(max(dp[N-1]))

=======
Suggestion 10

def main():
    N = int(input())
    snuke = [list(map(int, input().split())) for _ in range(N)]
    # print(snuke)
    time = 0
    snuke_sum = 0
    for i in range(N):
        if snuke[i][0] - time >= abs(snuke[i][1]):
            time = snuke[i][0]
            snuke_sum += snuke[i][2]
        elif snuke[i][0] - time < abs(snuke[i][1]) and snuke[i][1] < 0:
            time = snuke[i][0]
            snuke_sum += snuke[i][2]
        elif snuke[i][0] - time < abs(snuke[i][1]) and snuke[i][1] > 0:
            time = snuke[i][0]
            snuke_sum += snuke[i][2]
        else:
            continue
    print(snuke_sum)
