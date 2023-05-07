def get_input():
    H, W = [int(x) for x in input().split()]
    S = [input() for i in range(H)]
    return H, W, S

if __name__ == '__main__':
    get_input()