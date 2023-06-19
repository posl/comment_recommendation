def findMinDiff(A, B, n, m):
    A.sort()
    B.sort()
    a = 0
    b = 0
    result = 999999999999
    while(a<n and b<m):
        if(abs(A[a]-B[b])<result):
            result = abs(A[a]-B[b])
        if(A[a]>B[b]):
            b+=1
        else:
            a+=1
    return result

if __name__ == '__main__':
    findMinDiff()