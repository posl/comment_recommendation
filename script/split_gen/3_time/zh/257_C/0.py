def isChild(num, weight, s):
    i = 0
    for i in range(len(s)):
        if s[i] == '0':
            if weight[i] >= num:
                return False
        else:
            if weight[i] < num:
                return False
    return True
