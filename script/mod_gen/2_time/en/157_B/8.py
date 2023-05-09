def bingo(A, N, B):
    count = 0
    bingo = False
    for i in range(3):
        for j in range(3):
            if A[i][j] in B:
                count += 1
                if count == 3:
                    bingo = True
                    break
        count = 0
    for i in range(3):
        for j in range(3):
            if A[j][i] in B:
                count += 1
                if count == 3:
                    bingo = True
                    break
        count = 0
    for i in range(3):
        if A[i][i] in B:
            count += 1
            if count == 3:
                bingo = True
                break
    count = 0
    for i in range(3):
        if A[i][2-i] in B:
            count += 1
            if count == 3:
                bingo = True
                break
    return bingo

if __name__ == '__main__':
    bingo()