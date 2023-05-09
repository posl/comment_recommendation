def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B_C = [0] * N
    for i, c in enumerate(C):
        B_C[c - 1] += 1
    A_B_C = [0] * N
    for i, b in enumerate(B):
        A_B_C[A[i] - 1] += B_C[i]
    print(sum(A_B_C))
