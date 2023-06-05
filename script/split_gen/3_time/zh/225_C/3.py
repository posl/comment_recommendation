def is_submatrix(a, b):
    for i in range(len(a)-len(b)+1):
        for j in range(len(a[0])-len(b[0])+1):
            if a[i][j] == b[0][0]:
                if a[i:i+len(b)] == b:
                    return True
    return False
