def get_input():
    input_line = input().split()
    H = int(input_line[0])
    W = int(input_line[1])
    X = int(input_line[2])
    Y = int(input_line[3])
    S = []
    for i in range(H):
        S.append(input())
    return H, W, X, Y, S
