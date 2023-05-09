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

if __name__ == '__main__':
    main()