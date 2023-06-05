def get_input():
    N, M = map(int, input().split())
    k = []
    x = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    return N, M, k, x

if __name__ == '__main__':
    get_input()