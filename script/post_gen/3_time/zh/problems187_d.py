Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N-1, -1, -1):
        if (A[i]+ans) % B[i] != 0:
            ans += B[i] - (A[i]+ans) % B[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()

    if N % 2 == 0:
        a = A[N//2 - 1] + A[N//2]
        b = B[N//2 - 1] + B[N//2]
        print(b-a+1)
    else:
        a = A[N//2]
        b = B[N//2]
        print(b-a+1)

=======
Suggestion 3

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    ans = 0
    for i in range(N):
        if A[i] < B[i]:
            ans += 1
    print(ans)

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
    A.sort(reverse=True)
    B.sort(reverse=True)
    ans = 0
    for i in range(N):
        if A[i] > B[i]:
            ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    # 读入数据
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # 按照高桥能得到的票数排序
    AB.sort(key=lambda x: 2 * x[0] + x[1], reverse=True)
    # 高桥得到的票数
    total = sum([x[0] for x in AB])
    # 需要发表演讲的镇数
    cnt = 0
    # 直到高桥得到的票数超过青木的票数
    for i in range(N):
        total -= AB[i][0] + AB[i][1]
        cnt += 1
        if total < 0:
            break
    print(cnt)

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for i in range(n):
        ans += a[i] * i + b[i] * (n - i - 1)
    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    a.sort()
    b.sort()

    print(a[-1] + b[-1])

solve()

=======
Suggestion 8

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
    if n % 2 == 0:
        print(b[n//2-1] - a[n//2-1] + 1)
    else:
        print(b[n//2] - a[n//2] + 1)

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort(reverse=True)
    b.sort(reverse=True)
    a_sum = sum(a)
    b_sum = sum(b)
    a_count = 0
    b_count = 0
    for i in range(n):
        a_count += a[i]
        b_count += b[i]
        if a_count > b_count:
            print(i+1)
            break
        elif i == n-1:
            print(n)

main()

=======
Suggestion 10

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for i in range(n):
        if a[i] > b[i]:
            ans += 1
    print(ans)
