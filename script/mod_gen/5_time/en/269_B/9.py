def main():
    # input process
    S = [input() for i in range(10)]
    # process
    i = 0
    while i < 10:
        if S[i][0] == '.':
            i += 1
        else:
            break
    A = i+1
    i = 9
    while i >= 0:
        if S[i][9] == '.':
            i -= 1
        else:
            break
    B = i+1
    j = 0
    while j < 10:
        if S[0][j] == '.':
            j += 1
        else:
            break
    C = j+1
    j = 9
    while j >= 0:
        if S[9][j] == '.':
            j -= 1
        else:
            break
    D = j+1
    # output process
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    main()