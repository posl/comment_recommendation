def get_input():
    N = int(input())
    X, Y, H = [], [], []
    for _ in range(N):
        x, y, h = map(int, input().split())
        X.append(x)
        Y.append(y)
        H.append(h)
    return N, X, Y, H

if __name__ == '__main__':
    get_input()