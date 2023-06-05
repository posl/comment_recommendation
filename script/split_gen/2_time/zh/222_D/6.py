def get_input():
    n,m = map(int,input().split())
    a = [list(input()) for _ in range(2*n)]
    return n,m,a
