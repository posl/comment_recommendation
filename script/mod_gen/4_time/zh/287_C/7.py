def get_input():
    N, M = input().split()
    N = int(N)
    M = int(M)
    print(N, M)
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = input().split()
        u[i] = int(u[i])
        v[i] = int(v[i])
        print(u[i], v[i])
    return N, M, u, v

if __name__ == '__main__':
    get_input()