def main():
    X,K = map(int,input().split())
    for i in range(K):
        X = (X+5)//10*10
    print(X)
