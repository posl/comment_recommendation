def solve(n,k,ab):
    ab.sort(key=lambda x:x[0])
    sum = k
    for i in range(n):
        if sum >= ab[i][0]:
            sum += ab[i][1]
        else:
            return sum
    return sum
