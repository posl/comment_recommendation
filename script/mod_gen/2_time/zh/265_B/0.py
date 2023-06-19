def get_input():
    N, M, T = input().split()
    N = int(N)
    M = int(M)
    T = int(T)
    A = input().split()
    A = [int(i) for i in A]
    XY = []
    for i in range(M):
        XY.append(input().split())
        XY[i][0] = int(XY[i][0])
        XY[i][1] = int(XY[i][1])
    return N, M, T, A, XY

if __name__ == '__main__':
    get_input()