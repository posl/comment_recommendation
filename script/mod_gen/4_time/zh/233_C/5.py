def get_input():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    return N, X, L

if __name__ == '__main__':
    get_input()