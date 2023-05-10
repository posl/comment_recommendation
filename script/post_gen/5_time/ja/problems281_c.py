Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    time = 0
    for i in range(n):
        if t < time + a[i]:
            print(i+1,t-time)
            break
        time += a[i]
    else:
        print(n,t-time)

=======
Suggestion 2

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    a = a * 2
    sum = 0
    for i in range(len(a)):
        sum += a[i]
        if sum >= t:
            print(i + 1, t - (sum - a[i]))
            break

=======
Suggestion 3

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    time = 0
    for i in a:
        time += i
    time = t % time
    if time == 0:
        time = a[n - 1]
    else:
        for i in range(n):
            if time > a[i]:
                time -= a[i]
            else:
                print(i + 1, time)
                break

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T -= 1
    sum = 0
    for i in range(N):
        sum += A[i]
    cnt = T // sum
    T -= cnt * sum
    for i in range(N):
        T -= A[i]
        if T < 0:
            print(i+1, -T)
            return

=======
Suggestion 5

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    time = 0
    for i in range(n):
        time += a[i]
        if time > t:
            print(i+1, t - time + a[i])
            break
    else:
        print(n, t - time + a[n-1])

=======
Suggestion 6

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    x = T % total
    for i in range(N):
        if x <= A[i]:
            print(i + 1, x)
            break
        x -= A[i]

=======
Suggestion 7

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    N,T = map(int,readline().split())
    A = list(map(int,readline().split()))
    sumA = sum(A)
    cnt = T//sumA
    T -= cnt*sumA
    cumsum = [0]*(N+1)
    for i in range(N):
        cumsum[i+1] = cumsum[i]+A[i]
    for i in range(N):
        if T > cumsum[i] and T <= cumsum[i+1]:
            print(i+1,T-cumsum[i])
            break
    return

=======
Suggestion 8

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    ans1 = T // sum(A)
    ans2 = T % sum(A)
    ans3 = 0
    for i in range(N):
        ans2 -= A[i]
        if ans2 >= 0:
            ans3 += A[i]
        else:
            break
    print(ans1 * N + i + 1, ans3 + A[i] - ans2)

=======
Suggestion 9

def main():
    # input
    N, T = map(int, input().split())
    As = list(map(int, input().split()))

    # compute
    time = 0
    for i in range(N):
        time += As[i]
        if time >= T:
            ans1 = i+1
            ans2 = T - (time - As[i])
            break

    # output
    print(ans1, ans2)

=======
Suggestion 10

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    t = t % a_sum
    for i in range(n):
        if t < a[i]:
            print(i+1, t)
            break
        t -= a[i]
