def find_permutation(n,m,a,b,c,d):
    if m==0:
        return True
    for i in range(n):
        for j in range(n):
            if i!=j:
                if (a[i][j] and not c[i][j]) or (not a[i][j] and c[i][j]):
                    return False
    return True

if __name__ == '__main__':
    find_permutation()