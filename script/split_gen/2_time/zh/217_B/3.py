def compare_str(a,b):
    if len(a) < len(b):
        return True
    elif len(a) > len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i] < b[i]:
                return True
            elif a[i] > b[i]:
                return False
    return False
