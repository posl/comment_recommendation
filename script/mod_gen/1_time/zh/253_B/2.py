def read_input():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    return H, W, S

if __name__ == '__main__':
    read_input()