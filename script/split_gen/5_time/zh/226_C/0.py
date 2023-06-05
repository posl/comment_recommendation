def get_input():
    n = int(input().strip())
    t = []
    k = []
    a = []
    for i in range(n):
        line = input().strip().split()
        t.append(int(line[0]))
        k.append(int(line[1]))
        a.append(list(map(int, line[2:])))
    return n, t, k, a
