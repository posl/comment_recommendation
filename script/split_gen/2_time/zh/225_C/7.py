def main():
    n,m = map(int,input().split())
    B = [list(map(int,input().split())) for _ in range(n)]
    A = [[(i-1)*7+j for j in range(1,8)] for i in range(1,10**100+1)]
    print('Yes' if B in A else 'No')
