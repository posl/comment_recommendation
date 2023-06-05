def get_input():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, m, edges

if __name__ == '__main__':
    get_input()