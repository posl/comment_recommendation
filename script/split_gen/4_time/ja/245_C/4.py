def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort()
    B.reverse()
    
    #print(A)
    #print(B)
    
    if A[0] + K < B[0]:
        print("No")
        return
    
    if A[0] > B[0]:
        print("No")
        return
    
    for i in range(1, N):
        if A[i] > B[i]:
            print("No")
            return
        if A[i] + K < B[i]:
            print("No")
            return
    print("Yes")
    return
