def get_input():
    H, W = map(int, input().split())
    C = []
    for h in range(H):
        C.append(list(input()))
    return H, W, C

if __name__ == '__main__':
    get_input()