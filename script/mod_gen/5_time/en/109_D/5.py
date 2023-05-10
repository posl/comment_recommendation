def get_input():
    H, W = map(int, input().strip().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().strip().split())))
    return H, W, A

if __name__ == '__main__':
    get_input()