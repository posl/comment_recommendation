def main():
    n = int(input())
    ladders = []
    for i in range(n):
        ladders.append(list(map(int, input().split())))
    ladders.sort(key=lambda x: x[0])
    max_floor = ladders[0][0] + ladders[0][1] - 1
    for i in range(1, n):
        if ladders[i][0] >= max_floor:
            max_floor = ladders[i][0] + ladders[i][1] - 1
        elif ladders[i][1] >= max_floor:
            max_floor = ladders[i][1] + ladders[i][0] - 1
    print(max_floor)

if __name__ == '__main__':
    main()