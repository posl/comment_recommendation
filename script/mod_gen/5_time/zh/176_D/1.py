def get_input():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    return H, W, C_h, C_w, D_h, D_w, S

if __name__ == '__main__':
    get_input()