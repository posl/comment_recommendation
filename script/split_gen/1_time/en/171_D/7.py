def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        B.append(list(map(int, input().split())))
    for i in range(Q):
        C.append(B[i][1])
        B[i] = B[i][0]
    sumA = sum(A)
    for i in range(Q):
        sumA += (C[i] - B[i]) * A.count(B[i])
        print(sumA)
