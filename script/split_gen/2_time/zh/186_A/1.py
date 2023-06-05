def get_input():
    line = input()
    n, m = line.split(' ')
    n = int(n)
    m = int(m)
    if m == 0:
        a = []
    else:
        line = input()
        a = line.split(' ')
        a = [int(x) for x in a]
    return n, m, a
