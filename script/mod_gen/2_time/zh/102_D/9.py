def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print("N:", N, "A:", A)
    #A = [3,2,4,1,2]
    #A = [10,71,84,33,6,47,23,25,52,64]
    #A = [1,2,3,1000000000,4,5,6]
    #N = 7
    #N = 10
    #N = 5
    #print("N:", N, "A:", A)
    B = [0] * (N + 1)
    C = [0] * (N + 1)
    D = [0] * (N + 1)
    E = [0] * (N + 1)
    for i in range(1, N + 1):
        B[i] = B[i - 1] + A[i - 1]
    for i in range(1, N + 1):
        C[i] = C[i - 1] + A[i - 1]
    for i in range(1, N + 1):
        D[i] = D[i - 1] + A[i - 1]
    for i in range(1, N + 1):
        E[i] = E[i - 1] + A[i - 1]
    #print("B:", B)
    #print("C:", C)
    #print("D:", D)
    #print("E:", E)
    #print("N:", N, "A:", A)
    #print("B:", B)
    #print("C:", C)
    #print("D:", D)
    #print("E:", E)
    #print("N:", N, "A:", A)
    #print("B:", B)
    #print("C:", C)
    #print("D:", D)
    #print("E:", E)
    #print("N:", N, "A:", A)
    #print("B:", B)
    #print("C:", C)
    #print("D:", D)
    #print("E:", E)
    #print("N:", N, "A:", A)
    #print("B:", B)
    #print("C:", C)

if __name__ == '__main__':
    main()