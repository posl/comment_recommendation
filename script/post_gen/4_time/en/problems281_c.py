Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        sum += a[i]
        if sum >= t:
            print(i+1, t-(sum-a[i-1]))
            break

=======
Suggestion 2

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    sum = 0
    for i in range(N):
        sum += A[i]
        if sum >= T:
            print(i+1, T - sum + A[i])
            break

main()

=======
Suggestion 3

def get_input():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    return n, t, a

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    i = 0
    while i < N and total + A[i] < T:
        total += A[i]
        i += 1
    print(i+1, T-total)

=======
Suggestion 5

def problems281_c():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    r = t % s
    for i in range(n):
        if r <= a[i]:
            print(i + 1, r)
            break
        r -= a[i]

=======
Suggestion 6

def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    T -= 1
    print((T // S + 1) % N + 1, T % S + 1)

solve()

=======
Suggestion 7

def main():
    # input
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    # compute
    time = 0
    count = 0
    for i in range(N):
        if time + A[i] <= T:
            time += A[i]
            count += 1
        else:
            break
    # output
    print(count, T-time)

=======
Suggestion 8

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T, A)
    time = 0
    for i in range(N):
        if T < time + A[i]:
            print(i + 1, T - time)
            break
        time += A[i]
        if i == N - 1:
            print(1, T - time)

=======
Suggestion 9

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    if t == total:
        print(n, 0)
        return
    t = t % total
    for i in range(n):
        if t < a[i]:
            print(i + 1, t)
            return
        t -= a[i]

=======
Suggestion 10

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    # t = 0 から t までの合計時間
    sum_a = sum(a)

    # t を sum_a で割った余り
    t = t % sum_a

    # t が 0 になったら n 番目の曲が再生されている
    if t == 0:
        print(n)
        return

    # t が 0 でない場合
    for i in range(n):
        # t が a[i] 以下になったら i + 1 番目の曲が再生されている
        if t <= a[i]:
            print(i + 1, t)
            return
        else:
            # t が a[i] を超える場合は、a[i] を引いて t を更新する
            t -= a[i]
