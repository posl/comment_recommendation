def main():
    s = [input() for i in range(9)]
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '.':
                continue
            for k in range(9):
                if s[i][k] == '.':
                    continue
                for l in range(9):
                    if s[l][j] == '.':
                        continue
                    if i == k and j == l:
                        continue
                    if i == l and j == k:
                        continue
                    if s[k][l] == '#':
                        ans += 1
    print(ans//2)

if __name__ == '__main__':
    main()