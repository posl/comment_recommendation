def main():
    s = []
    for i in range(9):
        s.append(input())
    #print(s)
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                for k in range(9):
                    for l in range(9):
                        if s[k][l] == "#":
                            for m in range(9):
                                for n in range(9):
                                    if s[m][n] == "#":
                                        for o in range(9):
                                            for p in range(9):
                                                if s[o][p] == "#":
                                                    if (i,j) != (k,l) and (i,j) != (m,n) and (i,j) != (o,p) and (k,l) != (m,n) and (k,l) != (o,p) and (m,n) != (o,p):
                                                        if (i,j) == (min(i,j,k,l,m,n,o,p),max(i,j,k,l,m,n,o,p)) and (k,l) == (min(i,j,k,l,m,n,o,p),max(i,j,k,l,m,n,o,p)+1) and (m,n) == (min(i,j,k,l,m,n,o,p)+1,max(i,j,k,l,m,n,o,p)) and (o,p) == (min(i,j,k,l,m,n,o,p)+1,max(i,j,k,l,m,n,o,p)+1):
                                                            count += 1
    print(count//24)
