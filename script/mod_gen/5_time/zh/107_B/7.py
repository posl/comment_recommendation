def get_input():
    H, W = map(int, input().split())
    a = []
    for _ in range(H):
        a.append(list(input()))
    return H, W, a

if __name__ == '__main__':
    get_input()