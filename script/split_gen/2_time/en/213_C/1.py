def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # 位置情報の取得
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    A = {A[i]: i for i in range(len(A))}
    B = {B[i]: i for i in range(len(B))}
    for i in range(N):
        print(A[A[i]]+1, B[B[i]]+1)
