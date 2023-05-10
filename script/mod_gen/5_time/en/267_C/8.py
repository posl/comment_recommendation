def max_subarray(A, M):
    max_val = 0
    for i in range(0,len(A)-M+1):
        max_val = max(max_val, sum([A[i+j]*(j+1) for j in range(0,M)]))
    return max_val
N, M = map(int, input().split())
A = list(map(int, input().split()))
print(max_subarray(A, M))

if __name__ == '__main__':
    max_subarray()