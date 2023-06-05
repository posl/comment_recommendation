def main():
    N = int(input())
    Snukes = []
    for i in range(N):
        Snukes.append(list(map(int, input().split())))
    # print(Snukes)
    max_sum = 0
    for i in range(N):
        if i == 0:
            max_sum = Snukes[i][2]
        else:
            if Snukes[i][0] - Snukes[i-1][0] >= abs(Snukes[i][1] - Snukes[i-1][1]):
                max_sum += Snukes[i][2]
            else:
                max_sum += Snukes[i][2] - (abs(Snukes[i][1] - Snukes[i-1][1]) - (Snukes[i][0] - Snukes[i-1][0]))
    print(max_sum)

if __name__ == '__main__':
    main()