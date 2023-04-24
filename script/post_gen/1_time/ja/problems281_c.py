Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T %= sum(A)
    for i in range(N):
        T -= A[i]
        if T < 0:
            print(i+1, A[i]+T)
            break

=======
Suggestion 2

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += A[i]
        if T <= sum:
            print(i + 1, T - (sum - A[i]))
            return

=======
Suggestion 3

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    t = T % S
    for i in range(N):
        if t - A[i] < 0:
            print(i+1, t)
            break
        t -= A[i]

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    time = sum(A)
    T %= time
    for i in range(N):
        if T - A[i] <= 0:
            print(i+1, T)
            break
        T -= A[i]

=======
Suggestion 5

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    if T <= sum(A):
        for i in range(N):
            if T <= A[i]:
                print(i+1, T)
                break
            else:
                T -= A[i]
    else:
        T %= sum(A)
        for i in range(N):
            if T <= A[i]:
                print(i+1, T)
                break
            else:
                T -= A[i]

=======
Suggestion 6

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    count = T // sum_A
    T = T - (sum_A * count)
    for i in range(N):
        if T - A[i] <= 0:
            print(i+1, T)
            break
        else:
            T -= A[i]

=======
Suggestion 7

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T)
    #print(A)
    #print(sum(A))
    #print(T%sum(A))
    #print(T//sum(A))
    #print(N*T//sum(A))
    #print(T%sum(A) + N*T//sum(A))
    #print(T%sum(A) + N*T//sum(A) - N)
    #print((T%sum(A) + N*T//sum(A) - N) % N)
    #print((T%sum(A) + N*T//sum(A) - N) % N + 1)
    #print((T%sum(A) + N*T//sum(A) - N) % N + 1, ((T%sum(A) + N*T//sum(A) - N) // N) % A[(T%sum(A) + N*T//sum(A) - N) % N])
    ans = (T%sum(A) + N*T//sum(A) - N) % N + 1, ((T%sum(A) + N*T//sum(A) - N) // N) % A[(T%sum(A) + N*T//sum(A) - N) % N]
    #print(ans)
    print(*ans)

=======
Suggestion 8

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T)
    #print(A)
    total = sum(A)
    #print(total)
    if T % total == 0:
        print(N, 0)
        return
    else:
        T = T % total
        #print(T)
        for i, a in enumerate(A):
            if T <= a:
                print(i + 1, T)
                return
            else:
                T -= a
        return

=======
Suggestion 9

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    # プレイリストの長さ
    playlist_len = sum(A)

    # T秒後に流れている曲の番号
    song_num = T // playlist_len

    # T秒後に流れている曲が流れ始めてから何秒か
    song_time = T % playlist_len

    # T秒後に流れている曲が流れ始めてから何秒かを計算
    for i in range(N):
        if song_time >= A[i]:
            song_time -= A[i]
        else:
            print(i+1, song_time)
            break

=======
Suggestion 10

def playlist(N, T, A):
    # write your code here
    return 0, 0
