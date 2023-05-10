def check(fld):
    cnt = 0
    for i in range(9):
        for j in range(9):
            if fld[i][j] == "#":
                cnt += 1
    return cnt

if __name__ == '__main__':
    check()