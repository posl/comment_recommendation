def main():
    # input
    S = [list(input()) for _ in range(10)]
    # compute
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if i == 0:
                    if j == 0:
                        S[i][j] = 'A'
                    elif j == 9:
                        S[i][j] = 'C'
                    else:
                        S[i][j] = 'B'
                elif i == 9:
                    if j == 0:
                        S[i][j] = 'G'
                    elif j == 9:
                        S[i][j] = 'I'
                    else:
                        S[i][j] = 'H'
                else:
                    if j == 0:
                        S[i][j] = 'D'
                    elif j == 9:
                        S[i][j] = 'F'
                    else:
                        S[i][j] = 'E'
    # output
    for i in range(10):
        print(''.join(S[i]))
