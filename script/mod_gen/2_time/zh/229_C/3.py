def main():
    N, W = map(int, input().split())
    cheese = []
    for i in range(N):
        cheese.append(list(map(int, input().split())))
    cheese.sort(key=lambda x: x[0])
    sum = 0
    for i in range(N):
        if cheese[i][1] >= W:
            sum += cheese[i][0] * W
            break
        else:
            sum += cheese[i][0] * cheese[i][1]
            W -= cheese[i][1]
    print(sum)

if __name__ == '__main__':
    main()