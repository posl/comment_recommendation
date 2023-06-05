def main():
    n = int(input())
    list = []
    for i in range(n):
        list.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                list[i].append(1)
            else:
                list[i].append(list[i - 1][j - 1] + list[i - 1][j])
    for i in range(n):
        for j in range(i + 1):
            print(list[i][j], end=" ")
        print()

if __name__ == '__main__':
    main()