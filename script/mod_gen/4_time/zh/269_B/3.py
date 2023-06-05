def main():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                print(i + 1, j + 1)
                return

if __name__ == '__main__':
    main()