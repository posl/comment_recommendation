def main():
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        line = input().split()
        T.append(int(line[0]))
        K.append(int(line[1]))
        A.append([])
        for j in range(K[i]):
            A[i].append(int(line[2+j]))
    #print(T)
    #print(K)
    #print(A)
    D = [0] * N
    for i in range(N):
        if K[i] == 0:
            D[i] = T[i]
        else:
            D[i] = T[i] + max([D[j] for j in A[i]])
    print(max(D))
main()
