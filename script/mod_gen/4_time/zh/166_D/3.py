def solve(x):
    a = 0
    b = 0
    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            if i**5 - j**5 == x:
                a = i
                b = j
                break
        if a != 0:
            break
    return a, b

if __name__ == '__main__':
    solve()