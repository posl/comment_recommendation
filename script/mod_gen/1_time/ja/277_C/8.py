def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    #print(AB)
    max_floor = 0
    for i in range(N):
        if max_floor < AB[i][0]:
            max_floor = AB[i][0]
        if max_floor < AB[i][1]:
            max_floor = AB[i][1]
    print(max_floor)

if __name__ == '__main__':
    main()