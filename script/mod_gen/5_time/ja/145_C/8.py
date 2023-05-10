def main():
    N = int(input())
    towns = [list(map(int, input().split())) for _ in range(N)]
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += ((towns[i][0] - towns[j][0])**2 + (towns[i][1] - towns[j][1])**2)**0.5
    print(sum * 2 * math.factorial(N-1) / math.factorial(N))

if __name__ == '__main__':
    main()