def get_input():
    # N M
    # A_0 A_1 ...A_{N-1} A_N
    # C_0 C_1 ...C_{N+M-1} C_{N+M}
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    return N, M, A, C

if __name__ == '__main__':
    get_input()