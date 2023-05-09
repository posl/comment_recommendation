def nC2(n):
    return n*(n-1)//2
N = int(input())
A = list(map(int,input().split()))
A.sort()
