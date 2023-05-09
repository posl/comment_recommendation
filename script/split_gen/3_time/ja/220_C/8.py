def main():
    N=int(input())
    A=list(map(int,input().split()))
    X=int(input())
    B=A
    sumB=sum(A)
    k=0
    while k<X:
        k+=N
        if sumB>0:
            k+=((X-k)//sumB)*N
        for i in range(N):
            k+=1
            if k>X:
                break
            B.append(A[i])
            if k==X:
                break
    print(k)
