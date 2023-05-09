def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    min_time = 10**5 * 2
    for i in range(N):
        for j in range(N):
            if i == j:
                time = AB[i][0] + AB[j][1]
            else:
                time = max(AB[i][0], AB[j][1])
            min_time = min(time, min_time)
    print(min_time)

if __name__ == '__main__':
    main()