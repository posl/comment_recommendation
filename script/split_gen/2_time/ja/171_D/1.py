def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    #Bの要素の値をキーとする辞書を作る
    D = {}
    for i in range(N):
        if A[i] in D:
            D[A[i]] += 1
        else:
            D[A[i]] = 1
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(Q):
        if B[i] in D:
            sum -= D[B[i]] * B[i]
            sum += D[B[i]] * C[i]
            if C[i] in D:
                D[C[i]] += D[B[i]]
            else:
                D[C[i]] = D[B[i]]
            del D[B[i]]
        print(sum)
