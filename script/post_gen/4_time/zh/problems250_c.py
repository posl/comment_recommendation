Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n, q, x):
    #print("n=", n, "q=", q, "x=", x)
    #print("x=", x)
    for i in range(1, q+1):
        #print("i=", i)
        #print("x[i-1]=", x[i-1])
        if x[i-1] == i:
            #print("x[i-1]=", x[i-1], "i=", i)
            x[i-1], x[i] = x[i], x[i-1]
        else:
            #print("x[i-1]=", x[i-1], "i=", i)
            x[i-1], x[i] = x[i], x[i-1]
            x[i], x[i+1] = x[i+1], x[i]
    return x

=======
Suggestion 2

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    x = [int(input()) for _ in range(q)]
    a = [i for i in range(1, n+1)]

    for i in range(q-1, -1, -1):
        a[i], a[i+1] = a[i+1], a[i]
        if x[i] != a[i]:
            a[i], a[i+1] = a[i+1], a[i]

    print(*a)

=======
Suggestion 4

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr

=======
Suggestion 5

def swap_ball(balls, i):
    tmp = balls[i]
    balls[i] = balls[i+1]
    balls[i+1] = tmp
    return balls

=======
Suggestion 6

def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

=======
Suggestion 7

def main():
    n,q = map(int,input().split())
    x = []
    for i in range(q):
        x.append(int(input()))
    ans = [i for i in range(1,n+1)]
    for i in range(q-1,-1,-1):
        ans[x[i]-1],ans[x[i]] = ans[x[i]],ans[x[i]-1]
    print(' '.join(map(str,ans)))

=======
Suggestion 8

def main():
    # 读取输入
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    balls = [i for i in range(N+1)]
    for i in range(Q):
        x = int(input())
        balls[x], balls[x+1] = balls[x+1], balls[x]
    print(*balls[1:])

=======
Suggestion 9

def main():
    pass
