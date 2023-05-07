def set_input():
    M = int(input())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    pieces = list(map(int, input().split()))
    return M, edges, pieces

if __name__ == '__main__':
    set_input()