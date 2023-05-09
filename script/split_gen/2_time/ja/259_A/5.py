def main():
    N,M,X,T,D = map(int,input().split())
    height = X * D + 1
    for i in range(X+1,N+1):
        height += D
        if i == M:
            break
    print(height)
