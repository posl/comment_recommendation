def main():
    r,c = map(int, input().split())
    S = []
    for i in range(r):
        S.append(list(input()))
    # print(S)
    max = 0
    for i in range(r):
        for j in range(c):
            if S[i][j] == '.':
                tmp = 0
                for k in range(i+1, r):
                    if S[k][j] == '#':
                        break
                    else:
                        tmp += 1
                for k in range(i-1, -1, -1):
                    if S[k][j] == '#':
                        break
                    else:
                        tmp += 1
                for k in range(j+1, c):
                    if S[i][k] == '#':
                        break
                    else:
                        tmp += 1
                for k in range(j-1, -1, -1):
                    if S[i][k] == '#':
                        break
                    else:
                        tmp += 1
                if tmp > max:
                    max = tmp
    print(max+1)

if __name__ == '__main__':
    main()