def main():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(list(map(int, input().split())))
    ladders.sort(key=lambda x: x[1])
    for i in range(N):
        if ladders[i][0] > ladders[i][1]:
            ladders[i][0], ladders[i][1] = ladders[i][1], ladders[i][0]
    floor = 1
    for i in range(N):
        if ladders[i][0] <= floor <= ladders[i][1]:
            floor = ladders[i][1]
    print(floor)

if __name__ == '__main__':
    main()