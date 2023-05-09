def get_input_data():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    return H, W, A

if __name__ == '__main__':
    get_input_data()