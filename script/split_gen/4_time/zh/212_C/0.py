def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    min_diff = 10**9
    i = 0
    j = 0
    while i<n and j<m:
        min_diff = min(min_diff,abs(A[i]-B[j]))
        if A[i]>B[j]:
            j += 1
        else:
            i += 1
    print(min_diff)
