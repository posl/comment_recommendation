def get_input():
    N, W = input().split()
    N = int(N)
    W = int(W)
    A = []
    B = []
    for i in range(N):
        a, b = input().split()
        A.append(int(a))
        B.append(int(b))
    return N, W, A, B

if __name__ == '__main__':
    get_input()