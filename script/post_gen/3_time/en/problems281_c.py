Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    T %= total
    for i in range(N):
        T -= A[i]
        if T < 0:
            print(i+1, -T)
            return

main()

=======
Suggestion 2

def main():
    N, T = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    sumA = sum(A)
    t = T % sumA
    for i in range(N):
        if t < A[i]:
            print(i+1)
            print(t)
            break
        t -= A[i]

=======
Suggestion 3

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = sum(A)
    i = T % sumA
    for j in range(N):
        i -= A[j]
        if i < 0:
            print(j + 1, A[j] + i)
            break

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    mod = T % total
    for i in range(N):
        if mod >= A[i]:
            mod -= A[i]
        else:
            print(i + 1, mod + A[i])
            return

=======
Suggestion 5

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    count = T // sum_A
    T = T % sum_A
    for i in range(N):
        if T <= A[i]:
            print(i + 1, T)
            break
        T -= A[i]

=======
Suggestion 6

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, T)
    # print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
        if T <= sum:
            print(i+1, T - (sum-A[i]))
            break

=======
Suggestion 7

def main():
    N, T = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A_sum = sum(A)
    r = T % A_sum
    for i in range(N):
        if r < A[i]:
            print(i+1, r)
            break
        r -= A[i]

=======
Suggestion 8

def find_song(N, T, A):
    total = 0
    for i in range(N):
        total += A[i]
        if total >= T:
            return i + 1, T - (total - A[i])

=======
Suggestion 9

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    song = 0
    time = 0
    for i in range(N):
        if T >= time + A[i]:
            song = i + 1
            time += A[i]
        else:
            break
    print(song, T - time)

=======
Suggestion 10

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    # 総再生時間
    total_time = sum(A)

    # T秒後の曲
    song = (T - 1) // total_time + 1

    # T秒後の曲の再生開始時刻
    start_time = total_time * (song - 1)

    # T秒後の曲の再生終了時刻
    end_time = total_time * song

    # T秒後の曲の再生終了時刻までの残り時間
    remaining_time = end_time - T

    # T秒後の曲の再生終了時刻までの残り時間を超えるまでの曲の再生時間
    for i in range(N):
        remaining_time -= A[i]
        if remaining_time < 0:
            print(i + 1, T - start_time)
            break
