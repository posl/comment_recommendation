def solve(num):
    res = []
    while num > 0:
        if num % 2 == 0:
            num = num // 2
            res.append('B')
        else:
            num -= 1
            res.append('A')
    res.reverse()
    return ''.join(res)
print(solve(int(input())))
