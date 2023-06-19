def get_input():
    N, M = input().split()
    N = int(N)
    M = int(M)
    #print("N={0}, M={1}".format(N, M))
    A = []
    B = []
    for i in range(M):
        a, b = input().split()
        a = int(a)
        b = int(b)
        A.append(a)
        B.append(b)
    #print("A={0}, B={1}".format(A, B))
    return N, M, A, B

if __name__ == '__main__':
    get_input()