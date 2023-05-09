def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = [[A[i],i+1] for i in range(len(A))]
    while(len(A)!=2):
        A = [[max(A[2*i][0],A[2*i+1][0]),A[2*i][1]] if A[2*i][0]>A[2*i+1][0] else [max(A[2*i][0],A[2*i+1][0]),A[2*i+1][1]] for i in range(len(A)//2)]
    A = [A[0],A[1]]
    A.sort()
    print(A[0][1])
