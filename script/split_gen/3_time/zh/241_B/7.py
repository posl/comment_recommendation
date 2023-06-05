def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    #print(A)
    #print(B)
    if n < m:
        print('No')
    else:
        A.sort(reverse=True)
        B.sort(reverse=True)
        #print(A)
        #print(B)
        for i in range(m):
            if A[i] < B[i]:
                print('No')
                break
        else:
            print('Yes')
