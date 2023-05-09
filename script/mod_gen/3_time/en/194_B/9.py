def main():
    N = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    min_time = 10**6
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, AB[i][0] + AB[j][1])
            else:
                min_time = min(min_time, max(AB[i][0], AB[j][1]))
    print(min_time)

if __name__ == '__main__':
    main()