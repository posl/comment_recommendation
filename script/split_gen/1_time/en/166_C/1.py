def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    good = [True for i in range(N)]
    for i in range(M):
        if H[A[i]-1] <= H[B[i]-1]:
            good[A[i]-1] = False
        if H[B[i]-1] <= H[A[i]-1]:
            good[B[i]-1] = False
    
    print(sum(good))
