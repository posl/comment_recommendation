def check_sort(p):
    for i in range(len(p)-1):
        if p[i] > p[i+1]:
            return False
    return True
