Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, s, t):
    result = [0] * n
    for i in range(n):
        result[i] = t[i]
    for i in range(n - 1):
        if result[i + 1] > result[i] + s[i]:
            result[i + 1] = result[i] + s[i]
    for i in range(n):
        if result[i] > result[(i - 1) % n] + s[(i - 1) % n]:
            result[i] = result[(i - 1) % n] + s[(i - 1) % n]
    return result

=======
Suggestion 2

def main():
    n = int(input())
    s = list(map(int,input().split()))
    t = list(map(int,input().split()))
    ans = [0]*n
    for i in range(n):
        if i == 0:
            ans[i] = t[i]
        else:
            if ans[i-1] + s[i-1] > t[i]:
                ans[i] = ans[i-1] + s[i-1]
            else:
                ans[i] = t[i]
    for i in range(n):
        print(ans[i])

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    time = [0 for i in range(N)]
    time[0] = T[0]
    for i in range(1, N):
        if T[i] <= time[i-1]:
            time[i] = time[i-1] + S[i]
        else:
            time[i] = T[i]
    for i in range(N):
        print(time[i])

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int,input().split()))
    t = list(map(int,input().split()))
    #print(s)
    #print(t)
    if n == 1:
        print(t[0])
        return
    for i in range(n):
        if i == 0:
            if t[i] < s[i]:
                print(t[i])
            else:
                print(t[i]+s[i])
        else:
            if t[i] < s[i]:
                print(t[i])
            else:
                if t[i] == t[i-1]:
                    print(t[i]+s[i])
                else:
                    print(t[i] + s[i] - t[i-1])
    return

main()

=======
Suggestion 5

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0 for i in range(N)]
    for i in range(N):
        if i == 0:
            ans[i] = T[i]
        else:
            ans[i] = min(ans[i-1]+S[i-1], T[i])
    for i in range(N):
        print(ans[i])

=======
Suggestion 6

def solve(N, S, T):
    # N = int(input())
    # S = list(map(int, input().split()))
    # T = list(map(int, input().split()))
    # print(N, S, T)
    # N = 3
    # S = [4, 1, 5]
    # T = [3, 10, 100]
    # N = 4
    # S = [100, 100, 100, 100]
    # T = [1, 1, 1, 1]
    # N = 4
    # S = [1, 2, 3, 4]
    # T = [1, 2, 4, 7]
    # N = 8
    # S = [84, 87, 78, 16, 94, 36, 87, 93]
    # T = [50, 22, 63, 28, 91, 60, 64, 27]
    # print(N, S, T)
    # N = 200000
    # S = [1000000000]*N
    # T = [1]*N
    # print(N, S, T)
    # N = 200000
    # S = [1]*N
    # T = [1000000000]*N
    # print(N, S, T)

    # print(N, S, T)
    # N = 200000
    # S = [1000000000]*N
    # T = [1]*N
    # print(N, S, T)
    # N = 200000
    # S = [1]*N
    # T = [1000000000]*N
    # print(N, S, T)

    # N = 200000
    # S = [1000000000]*N
    # T = [1]*N
    # print(N, S, T)
    # N = 200000
    # S = [1]*N
    # T = [1000000000]*N
    # print(N, S, T)

    # N = 200000
    # S = [1000000000]*N
    # T = [1]*N
    # print(N

=======
Suggestion 7

def main():
    N = int(input())
    S = [int(i) for i in input().split()]
    T = [int(i) for i in input().split()]

    first = 0
    for i in range(N):
        if T[i] < T[first]:
            first = i

    ans = [0 for i in range(N)]
    ans[first] = T[first]
    for i in range(first+1, N):
        ans[i] = min(ans[i-1] + S[i-1], T[i])
    for i in range(first):
        ans[i] = min(ans[i-1] + S[i-1], T[i])

    for i in range(N):
        print(ans[i])

main()

=======
Suggestion 8

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[i] = t[i]
        else:
            ans[i] = min(t[i], ans[i - 1] + s[i - 1])
    for a in ans:
        print(a)

=======
Suggestion 9

def readinput():
    n=int(input())
    s=list(map(int,input().split()))
    t=list(map(int,input().split()))
    return n,s,t

=======
Suggestion 10

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    a = [[0 for i in range(2)] for j in range(N)]
    for i in range(N):
        a[i][0] = S[i]
        a[i][1] = T[i]
    a.sort(key=lambda x:x[1])
    for i in range(N):
        print(a[i][0])
