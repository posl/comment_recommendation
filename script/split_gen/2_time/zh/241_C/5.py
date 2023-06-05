def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    if n < m:
        print('No')
    else:
        for i in range(n):
            if A[i] < B[i]:
                print('No')
                return
        print('Yes')
