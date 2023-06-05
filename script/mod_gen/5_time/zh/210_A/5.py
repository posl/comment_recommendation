def problems210_a():
    N,A,X,Y = map(int,input().split())
    if N <= A:
        print(N * X)
    else:
        print(A * X + (N - A) * Y)

if __name__ == '__main__':
    problems210_a()