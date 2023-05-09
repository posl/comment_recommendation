def main():
    N,M,X,T,D = map(int, input().split())
    for i in range(M,X):
        T += D
    print(T)
