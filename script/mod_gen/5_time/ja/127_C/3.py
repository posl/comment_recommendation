def get_inputs():
    n, m = map(int, input().split())
    gates = []
    for i in range(m):
        gates.append(list(map(int, input().split())))
    return n, m, gates

if __name__ == '__main__':
    get_inputs()