def solve(s):
    s = list(s)
    count = 0
    for i in range(10000):
        i = '{:04}'.format(i)
        if all(si == 'o' or si == i.count(str(index)) for index, si in enumerate(s)):
            count += 1
    return count
