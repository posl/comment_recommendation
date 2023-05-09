def main():
    s = input()
    ans = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if s[0] == 'o' and i != 0:
                        continue
                    if s[1] == 'o' and j != 1:
                        continue
                    if s[2] == 'o' and k != 2:
                        continue
                    if s[3] == 'o' and l != 3:
                        continue
                    if s[4] == 'x' and i == 4:
                        continue
                    if s[5] == 'x' and j == 5:
                        continue
                    if s[6] == 'x' and k == 6:
                        continue
                    if s[7] == 'x' and l == 7:
                        continue
                    if s[8] == 'x' and i == 8:
                        continue
                    if s[9] == 'x' and j == 9:
                        continue
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()