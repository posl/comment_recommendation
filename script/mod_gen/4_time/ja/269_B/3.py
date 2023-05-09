def main():
    S = []
    for i in range(10):
        S.append(input())
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                print(i+1,j+1)
                exit()

if __name__ == '__main__':
    main()