Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    time = 0
    count = 0
    for i in range(N):
        if time + A[i] > T:
            break
        time += A[i]
        count += 1
    print(count + 1, T - time)

=======
Suggestion 2

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    count = (t // sum) * n
    t = t % sum
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum > t:
            print(count + i + 1, sum - a[i] - t)
            break

=======
Suggestion 3

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += A[i]
    num = T // total
    mod = T % total
    if mod == 0:
        mod = total
        num -= 1
    total = 0
    for i in range(N):
        total += A[i]
        if total >= mod:
            print(i + 1, mod - (total - A[i]))
            break

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += A[i]
    ans = (T // total) * N
    T %= total
    for i in range(N):
        if T >= A[i]:
            ans += 1
            T -= A[i]
        else:
            break
    print(ans, T)

=======
Suggestion 5

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    u = t % s
    c = 0
    for i in range(n):
        c += a[i]
        if u <= c:
            print(i+1, u)
            break

=======
Suggestion 6

def main():
    n, t = map(int, input().split())
    songs = list(map(int, input().split()))

    song = 0
    for i in range(n):
        t -= songs[i]
        if t < 0:
            song = i + 1
            t += songs[i]
            break

    print(song, t)

=======
Suggestion 7

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A)
    s = 0
    for i in range(N):
        s += A[i]
        if s > T:
            print(i)
            break
    else:
        print(N)

=======
Suggestion 8

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    c = t // s
    r = t % s
    a = a * 2
    for i in range(2 * n):
        r -= a[i]
        if r < 0:
            print(i + 1, -r)
            break

=======
Suggestion 9

def read_ints():
    return list(map(int, input().split()))

=======
Suggestion 10

def calc_song(N, T, A):
    song = 0
    time = 0
    for i in range(N):
        if time + A[i] > T:
            break
        time += A[i]
        song = i + 1
    time = T - time
    return song, time
