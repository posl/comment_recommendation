def problems259_a():
    N,M,X,T,D = map(int, input().split())
    h = T
    for i in range(1,X):
        h += D
    for i in range(X, N):
        h += D
    print(h)
problems259_a()

if __name__ == '__main__':
    problems259_a()