def problems138_c():
    n = 3
    v = [500, 300, 200]
    v.sort()
    while len(v) > 1:
        x = v.pop(0)
        y = v.pop(0)
        v.append((x + y) / 2)
        v.sort()
    print(v[0])

if __name__ == '__main__':
    problems138_c()