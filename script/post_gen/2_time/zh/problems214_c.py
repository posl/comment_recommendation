Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))
    S.insert(0,0)
    T.insert(0,0)
    for i in range(1,N+1):
        if i == 1:
            print(T[i])
        elif i == N:
            if T[i-1] + S[i-1] > T[i]:
                print(T[i])
            else:
                print(T[i-1] + S[i-1])
        else:
            if T[i-1] + S[i-1] > T[i]:
                print(T[i])
            else:
                print(T[i-1] + S[i-1])

=======
Suggestion 2

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    result = []
    for i in range(n):
        if i == 0:
            result.append(t[0])
        else:
            if t[i] < result[i-1]:
                result.append(t[i])
            else:
                result.append(t[i]+s[i])
    for i in result:
        print(i)

=======
Suggestion 3

def get_first_time(N, S, T):
    time = [0] * N
    for i in range(N):
        time[i] = T[i]
    for i in range(N):
        if (i == 0):
            if (S[i] > T[i]):
                time[i] = S[i]
        else:
            if (S[i] > T[i - 1] + S[i - 1]):
                time[i] = S[i]
            else:
                time[i] = T[i - 1] + S[i - 1] + S[i]
    return time

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0 for _ in range(n)]
    for i in range(n):
        if i == 0:
            if t[i] <= s[i]:
                ans[i] = t[i]
            else:
                ans[i] = s[i]
        else:
            if t[i] <= s[i] + ans[i-1]:
                ans[i] = t[i]
            else:
                ans[i] = s[i] + ans[i-1]
    for i in range(n):
        print(ans[i])

=======
Suggestion 5

def solve():
    pass

=======
Suggestion 6

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    time = [0] * n
    time[0] = t[0]
    for i in range(1, n):
        if time[i-1] + s[i-1] > t[i]:
            time[i] = time[i-1] + s[i-1]
        else:
            time[i] = t[i]
    for i in range(n):
        print(time[i])

=======
Suggestion 7

def solve(n, s, t):
    #print(n, s, t)
    for i in range(n):
        if s[i] < t[i]:
            s[i] += 10**9
    #print(s)
    for i in range(1, n):
        s[i] = min(s[i], s[i-1]+t[i-1])
    #print(s)
    return s

=======
Suggestion 8

def solve():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        if i == 0:
            ans[i] = T[i]
        else:
            ans[i] = min(T[i], ans[i - 1] + S[i - 1])
    for i in range(N):
        print(ans[i])


solve()

=======
Suggestion 9

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    print(S)
    print(T)
    time = [0] * N
    for i in range(N):
        time[i] = T[i]
    for i in range(N):
        if time[i] > time[i - 1] + S[i - 1]:
            time[i] = time[i - 1] + S[i - 1]
    for i in range(N):
        print(time[i])
