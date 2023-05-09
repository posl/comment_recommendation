def main():
    X,K=map(int,input().split())
    for i in range(K):
        X=round(X,-(i+1))
    print(X)
