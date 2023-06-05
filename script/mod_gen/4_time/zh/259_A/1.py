def problems259_a():
    n, m, x, t, d = map(int, input().split())
    height = t
    for i in range(1, n):
        if i < x:
            height += d
        elif i == x:
            continue
        else:
            height += d
    print(height)

if __name__ == '__main__':
    problems259_a()