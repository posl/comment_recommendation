def get_input():
    N, X, Y = map(int, input().split())
    tree = []
    for i in range(N - 1):
        tree.append(list(map(int, input().split())))
    return N, X, Y, tree

if __name__ == '__main__':
    get_input()