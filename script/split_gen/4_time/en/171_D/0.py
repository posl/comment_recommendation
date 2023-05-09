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
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(Q):
        sum = sum - (A[B[i]-1]*B.count(B[i])) + (C[i]*B.count(B[i]))
        print(sum)
