def main():
    # リストの入力
    S = [input() for i in range(9)]
    count = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                if i + 1 < 9 and j + 1 < 9:
                    if S[i + 1][j] == "#" and S[i][j + 1] == "#" and S[i + 1][j + 1] == "#":
                        count += 1
    print(count)

if __name__ == '__main__':
    main()