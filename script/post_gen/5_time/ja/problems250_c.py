Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    Y = list(range(1,N+1))

    for x in X:
        idx = Y.index(x)
        Y[idx], Y[idx+1] = Y[idx+1], Y[idx]

    print(*Y)

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    balls = [i for i in range(1, N+1)]
    for _ in range(Q):
        x = int(input())
        balls[x-1], balls[x] = balls[x], balls[x-1]
    print(*balls)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(range(1, N + 1))
    for _ in range(Q):
        x = int(input()) - 1
        A[x], A[x + 1] = A[x + 1], A[x]
    print(*A)

=======
Suggestion 4

def main():
    n,q = map(int,input().split())
    x = [i for i in range(n)]
    for i in range(q):
        a = int(input())
        x[a-1],x[a] = x[a],x[a-1]
    for i in range(n):
        print(x[i]+1,end=" ")
    print()

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    x = [int(input()) for _ in range(q)]
    a = [i for i in range(1, n+1)]
    for i in range(q):
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    print(*a)

=======
Suggestion 6

def main():
    N,Q = map(int,input().split())
    x = [int(input()) for _ in range(Q)]
    L = list(range(1,N+1))
    for i in range(Q):
        L[x[i]-1],L[x[i]] = L[x[i]],L[x[i]-1]
    print(*L)

=======
Suggestion 7

def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

N, Q = map(int, input().split())
balls = [i for i in range(1, N + 1)]
for _ in range(Q):
    x = int(input())
    if balls[x - 1] == x:
        continue
    if x == 1 or balls[x - 2] != x:
        balls[x - 1], balls[x] = swap(balls[x - 1], balls[x])
    else:
        balls[x - 2], balls[x - 1] = swap(balls[x - 2], balls[x - 1])
print(*balls)

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    x = [int(input()) for i in range(q)]
    a = [i for i in range(1, n+1)]
    for i in range(q):
        a[x[i]-1], a[x[i]] = a[x[i]], a[x[i]-1]
    print(' '.join(map(str, a)))

=======
Suggestion 9

def main():
    # 標準入力から N, Q を取得する
    N, Q = map(int, input().split())
    # 標準入力から x を取得する
    x = [int(input()) for _ in range(Q)]

    # 1 から N までの数値を配列に格納する
    a = list(range(1, N + 1))

    # x の値が a の中で何番目にあるかを取得する
    for i in range(Q):
        index = a.index(x[i])
        # x の値が a の最後の要素だった場合
        if index == N - 1:
            # a の最後の要素と a の最後から 2 番目の要素を入れ替える
            a[index], a[index - 1] = a[index - 1], a[index]
        # x の値が a の最後の要素以外だった場合
        else:
            # a の x の値がある場所と a の x の値の次の要素を入れ替える
            a[index], a[index + 1] = a[index + 1], a[index]

    # 結果を出力する
    print(*a)

=======
Suggestion 10

def main():
    # input
    N, Q = map(int, input().split())
    x = []
    for _ in range(Q):
        x.append(int(input()))

    # compute
    a = list(range(1, N+1))
    for i in range(Q):
        if i == 0:
            a[0], a[1] = a[1], a[0]
        else:
            if a.index(x[i]) == 0:
                a[0], a[1] = a[1], a[0]
            else:
                a[a.index(x[i])], a[a.index(x[i])-1] = a[a.index(x[i])-1], a[a.index(x[i])]

    # output
    print(*a)
