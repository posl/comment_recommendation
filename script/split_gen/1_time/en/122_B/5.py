def countACGT(s):
    count = 0
    for i in s:
        if i in 'ACGT':
            count += 1
        else:
            break
    return count
