Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, X = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    T = [A[i] + B[i] for i in range(N)]
    T2 = [A[i] * 2 + B[i] for i in range(N)]
    T2.sort()
    T.sort()
    for i in range(N - 1):
        T[i + 1] += T[i]
        T2[i + 1] += T2[i]
    ans = 10 ** 18
    for i in range(N):
        if i >= X:
            ans = min(ans, T[i - X] + (X - 1) * B[i])
        else:
            ans = min(ans, T2[i - X + 1] + (X - i - 1) * B[i])
    print(ans)
solve()

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = []
    b = []

    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    #print(a)
    #print(b)

    min_time = 10**18

    for i in range(n):
        time = 0
        for j in range(x):
            time += a[i] + b[i]*j
        if time < min_time:
            min_time = time

    print(min_time)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        v1, v2 = map(int, input().split())
        a.append(v1)
        b.append(v2)
    min_time = min(a)
    time = 0
    for i in range(n):
        time += a[i] + b[i]
    x -= n
    time += min_time * x
    print(time)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
    ans += X * min([AB[i][0] for i in range(N)])
    print(ans)

=======
Suggestion 5

def get_input():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    return n, x, a, b

=======
Suggestion 6

def solve():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    for a, b in AB:
        ans += a * b
        if ans > X:
            print(ans)
            return
    print(ans)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for i in range(N):
        ans += AB[i][0] + AB[i][1]
        if ans > X:
            print(i + 1)
            exit()
    print(-(-X // ans) * N)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0]+x[1])
    ans = 0
    for i in range(N):
        ans += AB[i][0]+AB[i][1]
        if ans > X:
            print(i+1)
            exit()
    print(N+1)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # 二分探索
    left = 0
    right = 10 ** 18
    while right - left > 1:
        mid = (left + right) // 2
        # mid 分以内に X 回クリアできるか
        cnt = 0
        for a, b in AB:
            cnt += 1
            if a > mid:
                continue
            # 映像を見る回数
            cnt += (mid - a) // b
        if cnt >= X:
            right = mid
        else:
            left = mid
    print(right)

=======
Suggestion 10

def solve(n,x,ab):
    t = [0]*n
    for i in range(n):
        t[i] = ab[i][0] + ab[i][1]
    for i in range(1,n):
        t[i] = min(t[i],t[i-1]+ab[i][1])
    ans = t[-1]*x
    for i in range(n-2,-1,-1):
        ans = min(ans,t[i]*x+(x-1)*ab[i+1][1])
    return ans
