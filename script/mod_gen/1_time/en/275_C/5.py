def main():
    S = [input() for _ in range(9)]
    ans = 0
    for i in range(8):
        for j in range(8):
            cnt = 0
            for k in range(2):
                for l in range(2):
                    if S[i+k][j+l] == "#":
                        cnt += 1
            if cnt == 4:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()