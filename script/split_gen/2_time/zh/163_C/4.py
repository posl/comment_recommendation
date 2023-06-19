def countSubordinates(i, subordinates):
    if len(subordinates[i]) == 0:
        return 0
    else:
        result = len(subordinates[i])
        for sub in subordinates[i]:
            result += countSubordinates(sub, subordinates)
        return result
