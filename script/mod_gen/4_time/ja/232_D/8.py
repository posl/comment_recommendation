def get_input_data():
    H, W = map(int, input().split())
    C = [list(input()) for i in range(H)]
    return H, W, C

if __name__ == '__main__':
    get_input_data()