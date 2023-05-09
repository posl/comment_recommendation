def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i] // 4
        A[i] = A[i] % 4
        if sum(A) >= 4:
            P += sum(A) // 4
            A = [a % 4 for a in A]
    print(P)
