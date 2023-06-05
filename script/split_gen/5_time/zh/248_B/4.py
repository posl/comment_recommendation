def solve(a,b,k):
    #print(a,b,k)
    if a >= b:
        return 0
    if k == 1:
        return b-a
    count = 0
    while a < b:
        a = a*k
        count += 1
    return count
