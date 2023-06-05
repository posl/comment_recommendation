def solve(a,b,c,d):
    max = 0
    for i in range(a,b+1):
        for j in range(c,d+1):
            if i*j > max:
                max = i*j
    return max
