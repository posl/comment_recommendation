def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    for i in range(N):
        AB[i][1] = AB[i][1] * 2
    cnt = 0
    for i in range(N):
        cnt += 1
        if cnt > X:
            break
        if AB[i][0] < AB[i][1]:
            AB[i][0] = AB[i][1]
        else:
            cnt -= 1
    if cnt > X:
        print(AB[i][0])
    else:
        print(AB[i][0] + AB[i][1] * (X - cnt))

if __name__ == '__main__':
    main()