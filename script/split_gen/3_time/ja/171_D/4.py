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
    S = sum(A)
    for i in range(Q):
        S += A.count(B[i])*(C[i]-B[i])
        print(S)
