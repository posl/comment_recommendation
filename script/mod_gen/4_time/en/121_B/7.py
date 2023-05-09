def get_input():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    return N, M, C, B, A

if __name__ == '__main__':
    get_input()