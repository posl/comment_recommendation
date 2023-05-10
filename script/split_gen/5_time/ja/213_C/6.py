def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A_sorted = sorted(A)
    B_sorted = sorted(B)
    A_dict = {}
    B_dict = {}
    for i in range(N):
        A_dict[A_sorted[i]] = i+1
        B_dict[B_sorted[i]] = i+1
    for i in range(N):
        print(A_dict[A[i]], B_dict[B[i]])
