def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted(A)
    B = sorted(B)
    for i in range(M):
        if A[i] < B[i]:
            print("No")
            return
    print("Yes")
