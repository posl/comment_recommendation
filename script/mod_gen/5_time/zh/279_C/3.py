def get_input():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    return H, W, S, T

if __name__ == '__main__':
    get_input()