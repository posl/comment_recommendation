def get_input():
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split(' '))
        T.append(t)
        X.append(x)
        A.append(a)
    return N, T, X, A

if __name__ == '__main__':
    get_input()