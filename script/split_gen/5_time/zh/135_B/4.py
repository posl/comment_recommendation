def check_sort(p):
    for i in range(len(p)):
        if p[i] != i + 1:
            return False
    return True
