def read_data():
    with open('problems099_d.txt') as f:
        lines = f.readlines()
        n, c = map(int, lines[0].split())
        D = [[0 for _ in range(c)] for _ in range(c)]
        for i in range(c):
            D[i] = list(map(int, lines[i+1].split()))
        C = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            C[i] = list(map(int, lines[i+1+c].split()))
    return n, c, D, C
