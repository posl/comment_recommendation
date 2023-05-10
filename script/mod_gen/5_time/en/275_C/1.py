def main():
    s = []
    for i in range(9):
        s.append(input())
    cnt = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()