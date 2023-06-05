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
    A_sum = sum(A)
    for i in range(Q):
        A_sum += (C[i] - B[i]) * A.count(B[i])
        print(A_sum)
