Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读入数据
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    # 计算答案
    t -= 1
    t %= sum(a)
    for i in range(n):
        if t < a[i]:
            break
        t -= a[i]

    # 打印答案
    print(i + 1, t + 1)

=======
Suggestion 2

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T = T % sum(A)
    sum = 0
    for i in range(N):
        if T < A[i]:
            print(i + 1, T)
            break
        else:
            T -= A[i]

=======
Suggestion 3

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    t %= sum
    for i in range(n):
        if t < a[i]:
            print(i+1, t)
            break
        t -= a[i]

main()

=======
Suggestion 4

def problem281_c():
    pass

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    t = t % total
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum >= t:
            print(i + 1, t)
            break

=======
Suggestion 7

def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T -= 1
    T %= sum(A)
    ans = 0
    while T >= A[ans]:
        T -= A[ans]
        ans += 1
    print(ans + 1, T + 1)

=======
Suggestion 8

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    for i in range(1, n+1):
        a[i] += a[i-1]
    t %= a[-1]
    for i in range(1, n+1):
        if a[i] > t:
            print(i, t-a[i-1])
            break

=======
Suggestion 9

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t = t % sum(a)
    for i in range(n):
        if t >= a[i]:
            t -= a[i]
        else:
            print(i+1, t)
            break
