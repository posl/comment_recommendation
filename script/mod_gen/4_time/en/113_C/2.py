def main():
    n, m = map(int, input().split())
    prefecture = [[] for i in range(n)]
    for i in range(m):
        p, y = map(int, input().split())
        prefecture[p-1].append([i, y])
    for i in range(n):
        prefecture[i].sort(key=lambda x: x[1])
        for j in range(len(prefecture[i])):
            prefecture[i][j].append(str(i+1).zfill(6))
            prefecture[i][j].append(str(j+1).zfill(6))
    for i in range(n):
        for j in range(len(prefecture[i])):
            print(''.join(prefecture[i][j][2:4]))

if __name__ == '__main__':
    main()