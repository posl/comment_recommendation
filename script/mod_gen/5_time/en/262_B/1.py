def get_input():
    N, M = map(int, input().split())
    U = []
    V = []
    for i in range(M):
        u, v = map(int, input().split())
        U.append(u)
        V.append(v)
    return N, M, U, V

if __name__ == '__main__':
    get_input()