Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n):
        if total + a[i] > t:
            print(i+1, t-total)
            break
        total += a[i]
        if i == n-1:
            print(1, t-total)

=======
Suggestion 2

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    sum = 0
    count = 0
    for a in A:
        sum += a
        if sum > T:
            break
        count += 1

    print(count, T - sum + A[count - 1])

=======
Suggestion 3

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += A[i]
    count = 0
    ans = 0
    for i in range(N):
        count += A[i]
        if count >= T:
            ans = i + 1
            break
    if count == T:
        print(ans, A[ans - 1])
    else:
        print(ans, A[ans - 1] - (count - T))

main()

=======
Suggestion 4

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    count = (t // sum) * n
    t %= sum
    for i in range(n):
        if a[i] > t:
            break
        else:
            t -= a[i]
            count += 1
    print(count + 1, t)

=======
Suggestion 5

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    time = 0
    for i in range(N):
        if time <= T:
            ans += 1
            time += A[i]
        else:
            break
    print(ans, time - A[ans - 1])

=======
Suggestion 6

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    for i in range(1, n):
        a[i] += a[i-1]
    print(t//a[n-1]*n + (next(i for i in range(n) if a[i] > t%a[n-1]) + 1) if t%a[n-1] in a else next(i for i in range(n) if a[i] > t%a[n-1]) + 1, t%a[n-1] if t%a[n-1] in a else t%a[n-1] - a[next(i for i in range(n) if a[i] > t%a[n-1]) - 1])

=======
Suggestion 7

def problem281_c():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    time = 0
    for i in range(N):
        if time + A[i] > T:
            print(i+1, T - time)
            return
        time += A[i]
    print((T//time)*N + 1, T - (T//time)*time)

=======
Suggestion 8

def main():
    n,t = map(int, input().split())
    a = list(map(int, input().split()))
    total = 0
    for i in range(n):
        total += a[i]
    c = t // total
    d = t % total
    e = 0
    for i in range(n):
        e += a[i]
        if e > d:
            print(i+1, d)
            break

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    # 1. 1回ループするまでの時間を求める
    total = 0
    for i in range(n):
        total += a[i]

    # 2. 1回ループする回数を求める
    count = t // total

    # 3. 1回ループした後に残る時間を求める
    remain = t % total

    # 4. 1回ループした後に残る時間を使って、何番目の曲が再生されているか求める
    index = 0
    for i in range(n):
        if remain >= a[i]:
            remain -= a[i]
            index += 1
        else:
            break

    # 5. 4.で求めた曲が何秒目に再生されているか求める
    time = remain

    print(index + 1, time)
