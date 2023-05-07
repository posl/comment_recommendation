def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        B.append(list(map(int, input().split())))
    #print(B)
    for i in range(Q):
        C.append(B[i][1])
    #print(C)
    sum_A = sum(A)
    #print(sum_A)
    for i in range(Q):
        if B[i][0] in A:
            sum_A = sum_A - B[i][0] * A.count(B[i][0]) + C[i] * A.count(B[i][0])
        print(sum_A)

if __name__ == '__main__':
    main()