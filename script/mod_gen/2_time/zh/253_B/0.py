def get_input():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    return H, W, S

if __name__ == '__main__':
    get_input()