Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, W = map(int, input().split())
    # 从1开始计算
    # 建立一个数组，记录��

=======
Suggestion 2

def main():
    n, w = map(int, input().split())
    a = [0] * 200010
    for i in range(n):
        s, t, p = map(int, input().split())
        a[s] += p
        a[t] -= p
    for i in range(1, 200010):
        a[i] += a[i - 1]
        if a[i] > w:
            print('No')
            return
    print('Yes')

=======
Suggestion 3

def main():
    n, w = map(int, input().split())
    a = []
    for i in range(n):
        s, t, p = map(int, input().split())
        a.append((s, p))
        a.append((t, -p))
    a.sort()
    s = 0
    for _, p in a:
        s += p
        if s > w:
            print("No")
            break
    else:
        print("Yes")

=======
Suggestion 4

def isEnoughWater(N, W, S, T, P):
    #按时间顺序，每次加水，判断是否满足
    #S, T, P = sorted(zip(S, T, P), key=lambda x:x[0])
    #print(S, T, P)
    #print(zip(S, T, P))
    #print(list(zip(S, T, P)))
    for i in range(N):
        water = 0
        for j in range(i + 1):
            if S[j] <= i and i < T[j]:
                water += P[j]
        if water > W:
            return False
    return True

=======
Suggestion 5

def main():
    n, w = map(int, input().split())
    a = [0] * 200001
    for i in range(n):
        s, t, p = map(int, input().split())
        a[s] += p
        a[t] -= p
    for i in range(1, 200001):
        a[i] += a[i - 1]
        if a[i] > w:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    n,w = map(int, input().split())
    a = []
    for i in range(n):
        s,t,p = map(int, input().split())
        a.append((s,p))
        a.append((t,-p))
    a.sort()
    for i in range(1,2*n):
        a[i] = (a[i-1][1]+a[i][1],a[i][0])
    for i in range(2*n):
        if a[i][0] > w:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    n, w = map(int, input().split())
    t = [0] * 200001
    for _ in range(n):
        s, e, p = map(int, input().split())
        t[s] += p
        t[e] -= p
    for i in range(1, 200001):
        t[i] += t[i-1]
        if t[i] > w:
            print('No')
            return
    print('Yes')

=======
Suggestion 8

def main():
    n, w = map(int, input().split())
    a = [0] * 200001
    for _ in range(n):
        s, t, p = map(int, input().split())
        a[s] += p
        a[t] -= p
    for i in range(1, 200001):
        a[i] += a[i - 1]
    if max(a) <= w:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n, w = map(int, input().split())
    events = []
    for _ in range(n):
        s, t, p = map(int, input().split())
        events.append((s, p))
        events.append((t, -p))
    events.sort()

    for _, p in events:
        w -= p
        if w < 0:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def solve():
    N, W = map(int, input().split())
    # 从0开始，所以要+1
    imos = [0] * (200001)
    for i in range(N):
        S, T, P = map(int, input().split())
        imos[S] += P
        imos[T] -= P
    for i in range(200001):
        if i > 0:
            imos[i] += imos[i - 1]
        if imos[i] > W:
            print("No")
            return
    print("Yes")
    return
