def lunlun(n):
    if n < 10:
        return True
    else:
        a = str(n)
        for i in range(len(a)-1):
            if abs(int(a[i]) - int(a[i+1])) > 1:
                return False
        return True
