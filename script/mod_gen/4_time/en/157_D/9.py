def make_set(parent, rank, n):
    parent[n] = n
    rank[n] = 0

if __name__ == '__main__':
    make_set()