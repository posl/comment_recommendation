def problems248_b(a,b,k):
    count = 0
    while a < b:
        a *= k
        count += 1
    return count
