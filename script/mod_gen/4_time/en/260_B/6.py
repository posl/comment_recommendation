def main():
    #N X Y Z
    #A_1 A_2 ... A_N
    #B_1 B_2 ... B_N
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append((A[i], B[i], i+1))
    C.sort(key=lambda x: -x[0])
    C = C[:X]
    C.sort(key=lambda x: -x[1])
    C = C[:X+Y]
    C.sort(key=lambda x: -(x[0]+x[1]))
    C = C[:X+Y+Z]
    C.sort(key=lambda x: x[2])
    for i in range(len(C)):
        print(C[i][2])

if __name__ == '__main__':
    main()