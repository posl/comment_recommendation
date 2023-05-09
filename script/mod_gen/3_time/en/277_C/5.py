def main():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(list(map(int, input().split())))
    ladders.sort(key=lambda x: x[0])
    max_floor = 0
    for i in range(N):
        if max_floor < ladders[i][1]:
            max_floor = ladders[i][1]
        else:
            max_floor = ladders[i][0]
    print(max_floor)

if __name__ == '__main__':
    main()