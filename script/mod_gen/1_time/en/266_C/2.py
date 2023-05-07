def isConvex(A, B, C, D):
    return (A[0] - D[0]) * (B[1] - D[1]) - (A[1] - D[1]) * (B[0] - D[0]) >= 0 and \
           (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0]) >= 0 and \
           (C[0] - B[0]) * (D[1] - B[1]) - (C[1] - B[1]) * (D[0] - B[0]) >= 0 and \
           (D[0] - C[0]) * (A[1] - C[1]) - (D[1] - C[1]) * (A[0] - C[0]) >= 0
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
print("Yes" if isConvex(A, B, C, D) else "No")

if __name__ == '__main__':
    isConvex()