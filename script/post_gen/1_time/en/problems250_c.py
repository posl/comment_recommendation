Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(range(1, N + 1))
    for _ in range(Q):
        x = int(input())
        i = A.index(x)
        if i == N - 1:
            A = A[:-1] + [x] + [A[-1]]
        else:
            A[i], A[i + 1] = A[i + 1], A[i]
    print(*A)

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]

    ans = [0] * N
    for i in range(N):
        ans[i] = i + 1

    for x in X:
        ans[x - 1], ans[x] = ans[x], ans[x - 1]

    print(*ans, sep='')

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    ball = [i for i in range(1, N + 1)]
    for _ in range(Q):
        x = int(input())
        ball[x - 1], ball[x] = ball[x], ball[x - 1]
    print(*ball)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    balls = [i for i in range(1, N+1)]
    for q in range(Q):
        x = int(input())
        index = balls.index(x)
        if index == len(balls)-1:
            balls[index] = balls[0]
            balls[0] = x
        else:
            balls[index] = balls[index+1]
            balls[index+1] = x
    print(*balls)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    ans = [i for i in range(N+1)]
    for i in range(Q-1, -1, -1):
        ans[x[i]], ans[x[i]+1] = ans[x[i]+1], ans[x[i]]
    for i in range(1, N+1):
        print(ans[i], end=' ')

main()

The code above is a solution for the above problem. The following is the explanation of the code.

=======
Suggestion 6

def main():
    #input
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]

    #compute
    balls = [i for i in range(1, N+1)]
    for x in X:
        i = balls.index(x)
        if i == N-1:
            balls[i], balls[i-1] = balls[i-1], balls[i]
        else:
            balls[i], balls[i+1] = balls[i+1], balls[i]

    #output
    print(*balls)

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]

    # 1-indexed
    a = [i for i in range(1, N+1)]

    # 1-indexed
    b = [i for i in range(1, N+1)]

    for i in range(Q):
        b[a[x[i]]] = a[x[i]-1]
        b[a[x[i]-1]] = a[x[i]]
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]

    for i in range(1, N+1):
        print(b[i], end=" ")

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]

    # N個の要素を持つリストを作成
    # 例：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = list(range(N))

    # x[i]の値をインデックスとして、a[i]とa[i+1]の値を入れ替える
    # 例：[1, 2, 3, 4, 5, 7, 6, 8, 10, 9]
    for i in range(Q):
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]

    # 1からNまでの整数をインデックスとして、a[i]の値を出力
    # 例：1 2 3 4 5 7 6 8 10 9
    for i in range(1, N+1):
        print(a[i-1]+1, end=' ')

=======
Suggestion 9

def main():
    # initialize
    N, Q = map(int, input().split())
    # swap_list = [0] * (N+1)
    swap_list = [i+1 for i in range(N)]
    swap_list[0] = 0
    swap_list[N] = 0
    # print(swap_list)
    for i in range(Q):
        x = int(input())
        # print("x=", x)
        # swap_list[x], swap_list[x+1] = swap_list[x+1], swap_list[x]
        # print("swap_list=", swap_list)
        swap_list[x], swap_list[x+1] = swap_list[x+1], swap_list[x]
        # print("swap_list=", swap_list)
    # print(swap_list)
    # print("swap_list[1:]= ", swap_list[1:])
    # print(*swap_list[1:])
    print(*swap_list[1:])

=======
Suggestion 10

def input():
    return sys.stdin.readline()[:-1]
