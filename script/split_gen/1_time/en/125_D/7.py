def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*N
    for i in range(N):
        B[i] = A[i]
        if i%2 == 1:
            B[i] *= -1
    C = [0]*N
    for i in range(N):
        C[i] = A[i]
        if i%2 == 0:
            C[i] *= -1
    Bsum = sum(B)
    Csum = sum(C)
    if Bsum < 0:
        Bsum *= -1
    if Csum < 0:
        Csum *= -1
    print(max(Bsum, Csum))
