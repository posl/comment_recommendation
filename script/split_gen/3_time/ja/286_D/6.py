def main():
    N, X = map(int,input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int,input().split())
    
    for i in range(N):
        for j in range(B[i]+1):
            if X == A[i] * j:
                print('Yes')
                return
    
    print('No')
    return
