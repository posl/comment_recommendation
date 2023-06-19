def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    AB.sort(key=lambda x: x[1])
    # print(AB)
    count = 0
    for i in range(M):
        if AB[i][0] == 1:
            count += 1
        else:
            break
    # print(count)
    if count == 0:
        print(0)
        exit()
    else:
        count += 1
    end = AB[count - 1][1]
    # print(end)
    for i in range(count, M):
        if AB[i][0] <= end:
            continue
        else:
            count += 1
            end = AB[i][1]
    print(count)

if __name__ == '__main__':
    main()