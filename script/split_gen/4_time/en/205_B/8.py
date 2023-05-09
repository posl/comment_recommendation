def check_permutation(a):
    a.sort()
    if a[0] == 1:
        for i in range(len(a)-1):
            if a[i+1] - a[i] != 1:
                return "No"
        return "Yes"
    else:
        return "No"
