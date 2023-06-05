def main():
    N, D = map(int, input().split())
    x = []
    for i in range(N):
        x.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            dis = 0
            for k in range(D):
                dis += (x[i][k] - x[j][k])**2
            if int(dis**0.5)**2 == dis:
                count += 1
    print(count)

if __name__ == '__main__':
    main()