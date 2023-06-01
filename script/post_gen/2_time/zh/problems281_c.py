Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #输入
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    #计算
    t = t % sum(a)
    #输出
    for i in range(n):
        if t < a[i]:
            print(i+1, t)
            break
        else:
            t -= a[i]

=======
Suggestion 2

def problem281_c():
    pass

=======
Suggestion 3

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T -= 1
    T = T % (sum(A))
    for i in range(N):
        if T < A[i]:
            print(i + 1, T)
            break
        else:
            T -= A[i]

=======
Suggestion 4

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t %= sum(a)
    s = 0
    for i in range(n):
        s += a[i]
        if t < s:
            print(i + 1, t)
            break

=======
Suggestion 5

def readIntList():
    return list(map(int, input().split()))

=======
Suggestion 6

def solve():
    pass

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    # 重复播放的时间
    loop = sum(a)
    # 重复播放的次数
    times = t // loop
    # 剩余时间
    rest = t % loop

    # 重复播放的次数内，播放的歌曲
    song = 0
    # 重复播放的次数内，播放的歌曲的时间
    song_time = 0
    for i in range(n):
        song_time += a[i]
        if song_time > rest:
            song = i + 1
            break

    # 剩余时间内，播放的歌曲
    song += times * n

    print(song, song_time)

=======
Suggestion 9

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t = t % (sum(a))
    s = 0
    for i in range(n):
        s += a[i]
        if t < s:
            print(i + 1, t)
            break

=======
Suggestion 10

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t = t % (sum(a))
    for i in range(n):
        if t < a[i]:
            print(i+1, t)
            break
        t -= a[i]
