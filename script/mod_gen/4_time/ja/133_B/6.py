def get_input():
    N, D = map(int, input().split())
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))
    return N, D, X

if __name__ == '__main__':
    get_input()