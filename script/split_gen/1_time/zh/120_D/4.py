def main():
    n,m = map(int,input().split())
    A = [0]*m
    B = [0]*m
    for i in range(m):
        A[i],B[i] = map(int,input().split())
    print(n,m,A,B)
