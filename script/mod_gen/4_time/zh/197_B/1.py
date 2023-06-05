def get_input():
    H, W, X, Y = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    return H, W, X, Y, S

if __name__ == '__main__':
    get_input()