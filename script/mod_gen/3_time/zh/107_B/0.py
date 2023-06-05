def get_input():
    H, W = input().split()
    H = int(H)
    W = int(W)
    a = []
    for i in range(H):
        a.append(input())
    return H, W, a

if __name__ == '__main__':
    get_input()