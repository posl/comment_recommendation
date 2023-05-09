def get_input():
    N, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    return N, W, A, B

if __name__ == '__main__':
    get_input()