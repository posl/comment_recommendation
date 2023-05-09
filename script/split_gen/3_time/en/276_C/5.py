def reverseList(a, start, end):
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
    return a
