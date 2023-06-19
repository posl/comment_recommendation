def get_input():
    N,M,T = input().split()
    N = int(N)
    M = int(M)
    T = int(T)
    A = input().split()
    A = [int(a) for a in A]
    XY = []
    for i in range(M):
        x,y = input().split()
        x = int(x)
        y = int(y)
        XY.append((x,y))
    return N, M, T, A, XY

if __name__ == '__main__':
    get_input()