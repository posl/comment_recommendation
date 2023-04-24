Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 360
    for i in range(N):
        ans = min(ans, 360 - sum(A[:i+1]))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 360
    for i in range(n):
        ans = min(ans, max(a[i], 360 - a[i]))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 360
    for i in range(N):
        B[A[i]] = 1
    for i in range(1, 360):
        B[i] += B[i-1]
    ans = 0
    for i in range(360):
        ans = max(ans, B[i])
        if i >= N:
            ans = max(ans, B[i] - B[i-N])
    print(360 - ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [A[i] - A[i-1] for i in range(1,N)]
    B.append(360 - A[N-1] + A[0])
    print(360 - max(B))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(360 - (sum(A) - N * 180))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)

    # 1 <= N <= 359
    # 1 <= A_i <= 359

    # 1 <= N <= 359
    # 1 <= A_i <= 359
    # 同じ場所に複数回切れ込みが入ることはない。

    # 1 <= N <= 359
    # 1 <= A_i <= 359
    # 同じ場所に複数回切れ込みが入ることはない。

    # 1 <= N <= 359
    # 1 <= A_i <= 359
    # 同じ場所に複数回切れ込みが入ることはない。

    # 1 <= N <= 359
    # 1 <= A_i <= 359
    # 同じ場所に複数回切れ込みが入ることはない。

    # 1 <= N <= 359
    # 1 <= A_i <= 359
    # 同じ場所に複数回切れ込みが入ることはない。

    # 1 <= N <= 359
    # 1 <= A_i <= 359
    # 同じ場所に複数回切れ込みが入ることはない。

    # 1 <= N <= 359
    # 1 <= A_i <= 359
    # 同じ場所に複数回切れ込みが入ることはない。

    # 1 <= N <= 359
    # 1 <= A_i <= 359
    # 同じ場所に複数回切れ込みが入ることはない。

    # 1 <= N <= 359
    # 1 <= A_i <= 359
    # 同じ場所に複数回切れ込みが入ることはない。

    # 1 <= N <= 359

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(360-min(A))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 最大の角度
    max_angle = 0
    # すべての角度の和
    sum_angle = 0
    # すべての角度の和が360の倍数でない場合は、360の倍数になるように調整する
    for i in range(N):
        sum_angle += A[i]
        if sum_angle % 360 == 0:
            max_angle = 360
            break
    # すべての角度の和が360の倍数の場合は、最大の角度を求める
    if max_angle == 0:
        # すべての角度の和を360で割った余り
        mod = sum_angle % 360
        # 余りを引いた角度
        angle = 360 - mod
        # 余りを引いた角度が最大の角度
        max_angle = angle

    print(max_angle)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)

    #最大の角度を求める
    max = 0
    for i in range(n):
        if max < a[i]:
            max = a[i]

    #print(max)

    #最大の角度との差が最小の角度を求める
    min = 360
    for i in range(n):
        if min > abs(max - a[i]):
            min = abs(max - a[i])

    print(360 - min)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 360度の中で最も大きな角度
    max_angle = 0
    # 360度の中で最も小さな角度
    min_angle = 360

    for i in range(N):
        # 360度の中で最も大きな角度の更新
        max_angle = max(max_angle, A[i])
        # 360度の中で最も小さな角度の更新
        min_angle = min(min_angle, A[i])

    # 最も大きなピザの中心角
    max_pizza_angle = 360 - (max_angle - min_angle)

    print(max_pizza_angle)
