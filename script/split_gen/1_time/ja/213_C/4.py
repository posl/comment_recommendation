def main():
    H,W,N = map(int,input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    A.sort()
    B.sort()
    for i in range(N):
        print(A[i] - bisect.bisect_left(A,A[i]) + 1,B[i] - bisect.bisect_left(B,B[i]) + 1)
