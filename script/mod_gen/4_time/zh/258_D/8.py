def main():
    N, X = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0] + x[1])
    min_time = 0
    for i in range(N):
        min_time += AB[i][0] + AB[i][1]
    if min_time > X:
        print(-1)
    else:
        count = 0
        for i in range(N):
            if min_time <= X:
                count += 1
                min_time += AB[i][0]
            else:
                break
        print(count)

if __name__ == '__main__':
    main()