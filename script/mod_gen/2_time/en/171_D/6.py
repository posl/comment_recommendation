def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    B = [0]*Q
    C = [0]*Q
    for i in range(Q):
        B[i], C[i] = [int(x) for x in input().split()]
    #print(N,A,Q,B,C)
    sumA = sum(A)
    #print(sumA)
    for i in range(Q):
        count = A.count(B[i])
        sumA = sumA + count*(C[i]-B[i])
        print(sumA)

if __name__ == '__main__':
    main()