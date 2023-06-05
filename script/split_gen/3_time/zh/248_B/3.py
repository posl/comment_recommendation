def slime(a,b,k):
    count = 0
    while a < b:
        a = a * k
        count += 1
    return count
