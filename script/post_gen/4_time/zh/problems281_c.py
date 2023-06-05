Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T -= 1
    T %= sum(A)
    a = 0
    for i in range(N):
        T -= A[i]
        if T < 0:
            a = i
            break
    print(a+1, T+A[a])

=======
Suggestion 2

def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    total = sum(a)
    t = t%total
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum >= t:
            print(i+1)
            break

=======
Suggestion 3

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    # print(n, t)
    # print(a)

    # t = t - 1
    # t = t % sum(a)
    # print(t)

    # for i in range(n):
    #     if t < a[i]:
    #         print(i+1, t)
    #         break
    #     t -= a[i]

    # print(a)
    t -= 1
    t %= sum(a)
    # print(t)
    for i in range(n):
        if t < a[i]:
            print(i+1, t)
            break
        t -= a[i]

=======
Suggestion 4

def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))

    #print(n,t)
    #print(a)

    i = 0
    while t > 0:
        t -= a[i]
        i += 1
        if i == n:
            i = 0

    print(i,t+a[i-1])

=======
Suggestion 5

def main():
    N,T = map(int, input().split())
    A = list(map(int, input().split()))
    T = T % sum(A)
    for i in range(N):
        if T <= A[i]:
            print(i+1, T)
            return
        else:
            T -= A[i]

=======
Suggestion 6

def get_next_song(song_num, song_list):
    if song_num >= len(song_list):
        return 1
    else:
        return song_num + 1

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    # 读入数据
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    # 模拟
    # 歌曲循环播放
    # 当前播放的歌曲编号
    cur = 0
    # 当前播放的歌曲已经播放的时间
    cur_time = 0
    while cur_time + a[cur] <= t:
        cur_time += a[cur]
        cur += 1
        if cur == n:
            cur = 0

    print(cur + 1, cur_time)

=======
Suggestion 9

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T = T % sum(A)
    for i in range(N):
        if T < A[i]:
            print(i + 1, T)
            exit()
        else:
            T -= A[i]
