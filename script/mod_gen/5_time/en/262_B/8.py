def get_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    return n, m, edges

if __name__ == '__main__':
    get_input()