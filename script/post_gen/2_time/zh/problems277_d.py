Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # 二分探索
    # 1. 試行回数はlog(10^9) = 30回
    # 2. 試行回数を減らすためには、その時点での最大値を使う
    # 3. 試行回数を減らすためには、その時点での最大値を使う
    # 4. 試行回数を減らすためには、その時点での最大値を使う
    # 5. 試行回数を減らすためには、その時点での最大値を使う
    # 6. 試行回数を減らすためには、その時点での最大値を使う
    # 7. 試行回数を減らすためには、その時点での最大値を使う
    # 8. 試行回数を減らすためには、その時点での最大値を使う
    # 9. 試行回数を減らすためには、その時点での最大値を使う
    # 10. 試行回数を減らすためには、その時点での最大値を使う
    ok = 10**9 + 1
    ng = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        # mid

=======
Suggestion 2

def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    ans = 1
    for i in range(N):
        if AB[i][0] < ans <= AB[i][1]:
            ans = AB[i][1] + 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    print(min(b) - max(a) + 1 if min(b) - max(a) + 1 > 0 else 0)

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 0:
        a = (A[N // 2 - 1] + A[N // 2]) // 2
        b = (B[N // 2 - 1] + B[N // 2]) // 2
        print(b - a + 1)
    else:
        a = A[N // 2]
        b = B[N // 2]
        print(b - a + 1)

=======
Suggestion 5

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int,input().split())))
    ab.sort(key = lambda x:x[0])
    #print(ab)
    for i in range(n):
        if i == 0:
            min = ab[i][0]
            max = ab[i][1]
        else:
            if ab[i][0] >= min and ab[i][0] <= max:
                min = ab[i][0]
                if ab[i][1] < max:
                    max = ab[i][1]
            else:
                print(ab[i][0]-1)
                return
    print(max)

=======
Suggestion 6

def solve():
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N)]
    ab.sort(key=lambda x: x[1])
    cur = 1
    for a, b in ab:
        if a <= cur <= b:
            cur = b
    print(cur)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    print(min(b) - max(a) + 1 if min(b) - max(a) + 1 > 0 else 0)

=======
Suggestion 8

def main():
    #n = int(input())
    #ab = [list(map(int, input().split())) for _ in range(n)]
    n = 3
    ab = [[500000000, 600000000], [600000000, 700000000], [700000000, 800000000]]

    ab.sort(key=lambda x: x[1])
    #print(ab)
    ans = 1
    for i in range(n):
        if ans < ab[i][0]:
            ans = ab[i][0]
        if ans >= ab[i][1]:
            ans = ab[i][1]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    
    if n == 1:
        print(max(a[0], b[0]))
        return
    
    a.sort()
    b.sort()
    a_max = a[-1]
    b_min = b[0]
    if a_max > b_min:
        print(0)
    else:
        print(b_min - a_max + 1)

=======
Suggestion 10

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        if a[i] > b[i]:
            ans = a[i]
            break
        elif i == n - 1:
            ans = b[-1] + 1
    print(ans)
