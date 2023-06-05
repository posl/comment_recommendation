def main():
    A,B,N = map(int,input().split())
    if A > B:
        print(B-1)
    else:
        print(int(A*N/B))
