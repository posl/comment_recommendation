def main():
    N = int(input())
    ladders = []
    for _ in range(N):
        ladders.append(tuple(map(int, input().split())))
    ladders.sort(key=lambda x: x[1])
    now = 1
    for i in range(N):
        if ladders[i][0] <= now:
            now = ladders[i][1]
        elif ladders[i][1] <= now:
            now = ladders[i][0]
    print(now)

if __name__ == '__main__':
    main()