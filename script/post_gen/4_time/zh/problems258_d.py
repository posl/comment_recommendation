Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, x, ab):
    a = []
    b = []
    for i in range(n):
        a.append(ab[i][0])
        b.append(ab[i][1])
    s = sum(a)
    t = sum(b)
    c = [2 * a[i] + b[i] for i in range(n)]
    c.sort()
    if s <= x:
        return n * (s + t)
    else:
        i = 0
        while i < n:
            if c[i] > x:
                break
            i += 1
        if i == n:
            return (n - 1) * x + t
        else:
            return i * x + (n - i) * (x + t)

=======
Suggestion 2

def main():
    n,x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(n):
        ans += a[i] + b[i]
    ans += min(a)
    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0] + x[1])

    ans = 0
    for i in range(N):
        ans += AB[i][0] + AB[i][1]
        if ans > X:
            print(i)
            return
    print(N)

=======
Suggestion 4

def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = float('inf')
    for i in range(N):
        t = X * A[i] + B[i]
        ans = min(ans, t)
    print(ans)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = float('inf')
    for i in range(n):
        ans = min(ans, x*i + b[i]*(n-i) + max(0, a[i]-b[i])*i)
    print(ans)

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]

    # def f(a,b,x):
    #     return a*x+b
    #
    # def f2(ab,x):
    #     return [f(a,b,x) for a,b in ab]
    #
    # def f3(ab,x):
    #     return sum(f2(ab,x))
    #
    # def f4(ab,x):
    #     return sum(f2(ab,x))/x
    #
    # def f5(ab,x):
    #     return sum(f2(ab,x))//x
    #
    # #print(f2(ab,x))
    # print(f3(ab,x))
    # print(f4(ab,x))
    # print(f5(ab,x))

    def f6(ab,x):
        return sum([a*x+b for a,b in ab])

    def f7(ab,x):
        return sum([a*x+b for a,b in ab])/x

    def f8(ab,x):
        return sum([a*x+b for a,b in ab])//x

    #print(f2(ab,x))
    print(f6(ab,x))
    print(f7(ab,x))
    print(f8(ab,x))

=======
Suggestion 7

def minTime(N, X, AB):
    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]
    AB = [(A[i], B[i]) for i in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    print(AB)
    # 二分查找
    left = 0
    right = 10 ** 18
    while left < right:
        mid = (left + right) // 2
        # print(left, mid, right)
        # 计算mid时间内可以通关的关卡数
        count = 0
        for i in range(N):
            # print(i, count, mid, AB[i][0] + AB[i][1])
            if mid >= AB[i][0] + AB[i][1]:
                count += 1
            else:
                break
        # print(count)
        if count >= X:
            right = mid
        else:
            left = mid + 1
    return left

=======
Suggestion 8

def solve():
    return 0

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0] + x[1])
    min_time = 0
    for i in range(N):
        min_time += AB[i][0] + AB[i][1]
    if min_time > X:
        print(-1)
    else:
        count = 0
        for i in range(N):
            if min_time <= X:
                count += 1
                min_time += AB[i][0]
            else:
                break
        print(count)

=======
Suggestion 10

def solve(N, X, A, B):
    # 二分法
    # 二分法的初始值
    left = 0
    right = 10 ** 18
    # 二分法的循环
    while right - left > 1:
        mid = (left + right) // 2
        # 检查mid是否满足条件
        if check(mid, N, X, A, B):
            right = mid
        else:
            left = mid
    return right
