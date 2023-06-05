def matrix_equal(a, b):
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if len(a[i]) != len(b[i]):
                return False
            else:
                for j in range(len(a[i])):
                    if a[i][j] != b[i][j]:
                        return False
        return True
