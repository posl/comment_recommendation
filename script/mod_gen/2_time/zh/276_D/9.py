def change(A):
    for i in range(len(A)-1,0,-1):
        if A[i-1]<A[i]:
            for j in range(len(A)-1,0,-1):
                if A[i-1]<A[j]:
                    A[i-1],A[j]=A[j],A[i-1]
                    A[i:]=A[len(A)-1:i-1:-1]
                    return A
    return A
N=int(input())
P=list(map(int,input().split()))
K=0
for i in range(1,N+1):
    K+=i*(N-1)**(i-1)
for i in range(K-1):
    P=change(P)
print(" ".join(map(str,P)))

if __name__ == '__main__':
    change()