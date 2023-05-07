def main():
    N,M,X,T,D = map(int, input().split())
    for i in range(M,N):
        if i == X:
            X += D
        T += X
    print(T)
