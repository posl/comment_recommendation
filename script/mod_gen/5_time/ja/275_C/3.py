def main():
    # input
    S = [input() for _ in range(9)]
    # compute
    ans = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                ans += 1
    ans = ans // 4
    # output
    print(ans)

if __name__ == '__main__':
    main()