def main():
    n, d = [int(i) for i in input().split()]
    x = [[int(i) for i in input().split()] for j in range(n)]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            dis = 0
            for k in range(d):
                dis += (x[i][k] - x[j][k]) ** 2
            if int(dis ** 0.5) ** 2 == dis:
                count += 1
    print(count)

if __name__ == '__main__':
    main()