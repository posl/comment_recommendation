def get_input():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    return N, M, A, B

if __name__ == '__main__':
    get_input()