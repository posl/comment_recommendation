def main():
    import sys
    input = sys.stdin.readline
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    for i in range(N-1):
        if abs(A[i]-A[i+1])>K and abs(B[i]-B[i+1])>K:
            if abs(A[i]-B[i+1])>K and abs(B[i]-A[i+1])>K:
                print("No")
                return
            else:
                if A[i]>B[i]:
                    A[i+1] = B[i+1]
                else:
                    B[i+1] = A[i+1]
        else:
            if abs(A[i]-B[i+1])<=K:
                A[i+1] = B[i+1]
            if abs(B[i]-A[i+1])<=K:
                B[i+1] = A[i+1]
    if A == B:
        print("Yes")
    else:
        print("No")
    return
