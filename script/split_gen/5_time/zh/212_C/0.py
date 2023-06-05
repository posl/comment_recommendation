def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    i,j = 0,0
    min = 1000000000
    while i < n and j < m:
        if A[i] < B[j]:
            if B[j] - A[i] < min:
                min = B[j] - A[i]
            i += 1
        else:
            if A[i] - B[j] < min:
                min = A[i] - B[j]
            j += 1
    print(min)
