def get_input():
    n = int(input())
    if n < 2 or n > 100000:
        raise Exception("n out of range")
    edge = []
    for i in range(n - 1):
        u, v, w = input().split()
        edge.append((int(u), int(v), int(w)))
    return n, edge

if __name__ == '__main__':
    get_input()