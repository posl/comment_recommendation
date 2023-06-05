Synthesizing 10/10 solutions

=======
Suggestion 1

def jump(x, n, a, b):
    if n == 0:
        return False
    if x == 0:
        return True
    if x < 0:
        return False
    return jump(x-a[0], n-1, a[1:], b[1:]) or jump(x-b[0], n-1, a[1:], b[1:])

=======
Suggestion 2

def solve():
    N, X = map(int, input().split())
    for i in range(N):
        a, b = map(int, input().split())
        if X == a or X == b or X == a + b:
            print('Yes')
            return
    print('No')

solve()

=======
Suggestion 3

def solve():
    N,X = map(int,input().split())
    a = [0]*N
    b = [0]*N
    for i in range(N):
        a[i],b[i] = map(int,input().split())
    if X < min(a):
        print('No')
        return
    if X >= max(b):
        print('Yes')
        return
    print('No')
    return

=======
Suggestion 4

def jump(n, x, ab):
    #print(n, x, ab)
    for i in range(n):
        if x >= ab[i][0] and x <= ab[i][1]:
            return 'Yes'
    return 'No'

=======
Suggestion 5

def jump(n, x, a, b):
    # 从最后一步开始跳，倒着推
    # 如果这一步跳a，那么前面的跳法就是n-1步跳到x-a
    # 如果这一步跳b，那么前面的跳法就是n-1步跳到x-b
    # 两种方式只要有一种成功，就可以
    if n == 0:
        return False
    if x == a[n-1] or x == b[n-1]:
        return True
    return jump(n-1, x-a[n-1], a, b) or jump(n-1, x-b[n-1], a, b)

=======
Suggestion 6

def main():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    for i in range(N):
        if X >= a[i] and X <= b[i]:
            print("Yes")
            exit()
    print("No")
main()

=======
Suggestion 7

def jump(n, x, a, b):
    i = 0
    while i < n:
        if x < a[i] or x > b[i]:
            return False
        i += 1
    return True

=======
Suggestion 8

def is_possible(N, X, a, b):
    x = 0
    for i in range(N):
        if x + a[i] <= X:
            x += b[i]
        else:
            x += a[i]
        if x == X:
            return True
    return False

=======
Suggestion 9

def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # print(a)
    # print(b)
    sum = 0
    for i in range(n):
        sum += a[i]
    if sum > x:
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def solve():
    n, x = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        if (x-a)%b == 0:
            print("Yes")
            return
    print("No")
