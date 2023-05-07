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
