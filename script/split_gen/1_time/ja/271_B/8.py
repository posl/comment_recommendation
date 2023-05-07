def main():
    N, Q = map(int, input().split())
    #N, Q = 3, 4
    #L = [4, 2, 3]
    #A = [[128, 741, 239, 901], [1, 1], [314, 159, 26535]]
    L = []
    A = []
    for i in range(N):
        l = list(map(int, input().split()))
        #l = A[i]
        L.append(l[0])
        A.append(l[1:])
    #print(L)
    #print(A)
    #print(N, Q)
    #print(A)
    #print(L)
    for i in range(Q):
        s, t = map(int, input().split())
        #s, t = A[i + N]
        print(A[s - 1][t - 1])
    #print(A)
main()
