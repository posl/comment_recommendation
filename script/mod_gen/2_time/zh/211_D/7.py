def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])
    #print(AB)
    count = 0
    now = 0
    for i in range(M):
        if AB[i][0] > now:
            count += 1
            now = AB[i][1]
        elif AB[i][1] < now:
            now = AB[i][1]
    print(count)

if __name__ == '__main__':
    main()