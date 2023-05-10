def make_palindrome(a):
    if len(a) == 1:
        return 0
    if len(a) == 2:
        if a[0] == a[1]:
            return 0
        else:
            return 1
    a.sort()
    count = 0
    i = 0
    j = len(a) - 1
    while i < j:
        if a[i] == a[j]:
            i += 1
            j -= 1
        elif a[i] < a[j]:
            a[i+1] = a[i] + a[i+1]
            count += 1
            i += 1
        else:
            a[j-1] = a[j] + a[j-1]
            count += 1
            j -= 1
    return count
