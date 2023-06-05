def main():
    list = []
    for i in range(10):
        list.append(input())
    for i in range(10):
        for j in range(10):
            if list[i][j] == '#':
                print(i+1, j+1)
                break
        else:
            continue
        break
    for i in range(9, -1, -1):
        for j in range(9, -1, -1):
            if list[i][j] == '#':
                print(i+1, j+1)
                break
        else:
            continue
        break

if __name__ == '__main__':
    main()