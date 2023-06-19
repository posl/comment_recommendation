Synthesizing 10/10 solutions

=======
Suggestion 1

def swap(a, b, li):
    tmp = li[a-1]
    li[a-1] = li[b-1]
    li[b-1] = tmp

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    a = [i for i in range(1, N+1)]
    for i in range(Q):
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    print(*a)

=======
Suggestion 3

def swap(a, b):
    return b, a

=======
Suggestion 4

def solve():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    x = x[::-1]
    ans = [i for i in range(N, 0, -1)]
    for i in range(Q):
        ans[x[i]-1], ans[x[i]] = ans[x[i]], ans[x[i]-1]
    print(*ans)
solve()

=======
Suggestion 5

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

=======
Suggestion 6

def get_input():
    input = raw_input()
    return input

=======
Suggestion 7

def swap(a, b):
    return b, a

N, Q = map(int, input().split())
balls = [i for i in range(1, N+1)]
for i in range(Q):
    x = int(input())
    balls[x-1], balls[x] = swap(balls[x-1], balls[x])
print(' '.join(map(str, balls)))

=======
Suggestion 8

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

=======
Suggestion 9

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

=======
Suggestion 10

def func1():
    N, Q = map(int, input().split())
    ball = [i+1 for i in range(N)]
    #print(ball)
    for i in range(Q):
        x = int(input())
        #print(x)
        index = ball.index(x)
        #print(index)
        if index != N-1:
            ball[index], ball[index+1] = ball[index+1], ball[index]
        else:
            ball[index], ball[0] = ball[0], ball[index]
        #print(ball)
    print(*ball)
