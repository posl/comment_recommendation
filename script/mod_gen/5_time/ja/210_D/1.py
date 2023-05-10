def get_input_data():
    # H, W, C
    input_line = input().split()
    H = int(input_line[0])
    W = int(input_line[1])
    C = int(input_line[2])
    # A
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    return H, W, C, A

if __name__ == '__main__':
    get_input_data()