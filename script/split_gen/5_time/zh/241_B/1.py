def solution():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if max(A) < max(B):
        print('No')
    else:
        print('Yes')
