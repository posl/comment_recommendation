def get_input():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split()))[1:])
    return N, M, A

if __name__ == '__main__':
    get_input()