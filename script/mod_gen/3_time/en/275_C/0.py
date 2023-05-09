def main():
    S = [input() for _ in range(9)]
    ans = 0
    for i in range(8):
        for j in range(8):
            if S[i][j] == S[i][j+1] == S[i+1][j] == S[i+1][j+1] == '#':
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()