def is_lunlun(n):
    n = str(n)
    for i in range(len(n)-1):
        if abs(int(n[i]) - int(n[i+1])) > 1:
            return False
    return True
