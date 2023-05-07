def main():
    N = int(input())
    x_y = []
    for i in range(N):
        x_y.append(list(map(int,input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if x_y[i][0] == x_y[j][0] and x_y[i][1] == x_y[k][1] and x_y[j][1] == x_y[k][0]:
                    count += 1
                elif x_y[i][0] == x_y[k][0] and x_y[i][1] == x_y[j][1] and x_y[k][1] == x_y[j][0]:
                    count += 1
                elif x_y[j][0] == x_y[k][0] and x_y[j][1] == x_y[i][1] and x_y[k][1] == x_y[i][0]:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()