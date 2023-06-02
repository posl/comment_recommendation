Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    a = sorted(a)
    ans = 0
    for i in range(n):
        if t < a[i]:
            ans = i
            break
        t -= a[i]
        ans = t // a[i]
        t %= a[i]
    print(ans+1, t)

=======
Suggestion 3

def main():
    num, time = map(int, input().split())
    songs = list(map(int, input().split()))
    time = time % sum(songs)

    for i in range(num):
        if time < songs[i]:
            print(i+1, time)
            break
        time -= songs[i]

=======
Suggestion 4

def get_next_song(song):
    global song_list
    global song_time
    global song_now
    global song_time_now
    song_now += 1
    if song_now == len(song_list):
        song_now = 0
    song_time_now = song_time[song_now]
    return song_list[song_now]

=======
Suggestion 5

def main():
    N,T = map(int,input().split())
    A = list(map(int,input().split()))
    sumA = sum(A)
    T = T % sumA
    sumA = 0
    for i in range(N):
        sumA += A[i]
        if sumA >= T:
            print(i+1,T)
            exit()

=======
Suggestion 6

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    t %= sum(a)
    for i in range(n):
        if t < a[i]:
            print(i + 1, t)
            break
        t -= a[i]

=======
Suggestion 7

def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    for i in range(n):
        count += a[i]
        if count >= t:
            print(i+1,t-(count-a[i]))
            break
    else:
        print((t-1)%n+1,t-(t-1)%n)

=======
Suggestion 8

def problems281_c():
    pass

=======
Suggestion 9

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t = t % sum(a)
    s = 0
    for i in range(n):
        s += a[i]
        if s > t:
            print(i + 1, t)
            exit()
