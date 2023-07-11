def judge(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if(i==j):
                continue
            if(a[i][j] == 'W' and a[j][i] != 'L'):
                return False
            if(a[i][j] == 'L' and
