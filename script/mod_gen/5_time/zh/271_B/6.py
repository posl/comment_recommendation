def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        A.append([int(i) for i in input().split()])
    B = []
    for i in range(Q):
        B.append([int(i) for i in input().split()])
    for i in range(Q):
        print(A[B[i][0]-1][B[i][1]-1])

if __name__ == '__main__':
    main()