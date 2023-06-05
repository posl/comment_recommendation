def main():
    num, time = map(int, input().split())
    songs = list(map(int, input().split()))
    time = time % sum(songs)
    for i in range(num):
        if time < songs[i]:
            print(i+1, time)
            break
        time -= songs[i]

if __name__ == '__main__':
    main()