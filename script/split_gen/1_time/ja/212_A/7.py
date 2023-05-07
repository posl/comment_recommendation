def judge(a,b):
    if a > 0 and b == 0:
        return 'Gold'
    elif a == 0 and b > 0:
        return 'Silver'
    elif a > 0 and b > 0:
        return 'Alloy'
    else:
        return 'Error'
