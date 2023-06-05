def get_input():
    line = raw_input()
    line = line.split()
    n = int(line[0])
    m = int(line[1])
    edges = []
    for i in range(m):
        line = raw_input()
        line = line.split()
        edges.append([int(line[0]), int(line[1])])
    return n, m, edges

if __name__ == '__main__':
    get_input()