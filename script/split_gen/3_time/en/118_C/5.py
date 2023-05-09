def main():
    N=int(input())
    A=list(map(int,input().split()))
    A.sort(reverse=True)
    h=A[0]
    for i in range(1,N):
        h=(h+A[i]-1)//A[i]*A[i]
    print(h)
