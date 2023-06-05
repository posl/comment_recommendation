def get_input():
    line = input()
    n, m = line.split()
    n = int(n)
    m = int(m)
    edges = []
    for i in range(m):
        line = input()
        u, v = line.split()
        u = int(u)
        v = int(v)
        edges.append((u, v))
    return n, m, edges

if __name__ == '__main__':
    get_input()