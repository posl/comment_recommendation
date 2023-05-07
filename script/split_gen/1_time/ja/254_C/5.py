def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    if K % 2 == 0:
        for i in range(N):
            if i % 2 == 0:
                if A[i] > A[i+1]:
                    A[i], A[i+1] = A[i+1], A[i]
            else:
                if A[i] < A[i+1]:
                    A[i], A[i+1] = A[i+1], A[i]
    else:
        for i in range(N):
            if i % 2 == 0:
                if A[i] < A[i+1]:
                    A[i], A[i+1] = A[i+1], A[i]
            else:
                if A[i] > A[i+1]:
                    A[i], A[i+1] = A[i+1], A[i]
    
    ans = True
    for i in range(N-1):
        if A[i] > A[i+1]:
            ans = False
            break
    if ans:
        print("Yes")
    else:
        print("No")
