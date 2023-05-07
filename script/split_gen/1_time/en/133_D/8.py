def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 3:
        print(A[2]//2, A[2]//2, A[0])
        return
    x = (A[0] + A[1] - A[N-1]) // 2
    B = [x]
    for i in range(1, N):
        B.append(A[i-1] - B[i-1])
    for i in range(N):
        print(B[i], end = " ")
    print()
