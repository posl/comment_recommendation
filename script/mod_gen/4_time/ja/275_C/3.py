def main():
    # input
    S = []
    for _ in range(9):
        S.append(input())
    # compute
    cnt = 0
    for r in range(9):
        for c in range(9):
            if S[r][c] == '#':
                if r-1 >= 0 and c-1 >= 0 and S[r-1][c-1] == '#':
                    if r-1 >= 0 and S[r-1][c] == '#':
                        if c-1 >= 0 and S[r][c-1] == '#':
                            cnt += 1
    # output
    print(cnt)

if __name__ == '__main__':
    main()