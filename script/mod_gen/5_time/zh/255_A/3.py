def problems255_a():
    R,C = map(int,input().split())
    A = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        A[i] = list(map(int,input().split()))
    print(A[R-1][C-1])

if __name__ == '__main__':
    problems255_a()