Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n,x = map(int, input().split())
    ans = 0
    for i in range(n):
        a,b = map(int, input().split())
        if a <= x <= b:
            ans += 1
    if ans > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def solve(n, x, a, b):
    for i in range(n):
        if i % 2 == 0:
            x -= a[i]
        else:
            x -= b[i]
    return x >= 0

n, x = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

=======
Suggestion 3

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(n):
        if x == a[i] or x == b[i]:
            print("Yes")
            break
        elif x < a[i]:
            print("No")
            break
        else:
            x = x - a[i]
            x = x + b[i]
            if i == n-1:
                print("Yes")

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    # print(a)
    # print(b)

    # 从后往前推
    # 最后一个跳跃
    if x == a[n-1] or x == b[n-1]:
        print('Yes')
        return

    # 倒数第二个跳跃
    if x > a[n-1] and x < b[n-1]:
        print('Yes')
        return

    # 倒数第三个跳跃
    if x > a[n-2] and x < b[n-2]:
        print('Yes')
        return

    # 倒数第四个跳跃
    if x > a[n-3] and x < b[n-3]:
        print('Yes')
        return

    print('No')

=======
Suggestion 5

def solve():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(N):
        if X < a[i] or X > b[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    # 输入
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # 判断
    sum = 0
    for i in range(N):
        if (i % 2 == 0):
            sum += b[i]
        else:
            sum += a[i]
    if (sum >= X):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def is_reach(x, a, b, n):
    if n == 0:
        return False
    if x == a[n-1] or x == b[n-1]:
        return True
    return is_reach(x - a[n-1], a, b, n-1) or is_reach(x - b[n-1], a, b, n-1)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(N):
        if X <= a[i]:
            print("No")
            return
        X += b[i] - a[i]
    print("Yes")

=======
Suggestion 10

def solve(n, x, a, b):
    for i in range(n):
        if x == a[i] or x == b[i]:
            return 'Yes'
    return 'No'
