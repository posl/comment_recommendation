def main():
    N,M,X,T,D = map(int,input().split())
    if M == 0:
        print(T)
    else:
        for i in range(M):
            if i < X-1:
                T += D
            elif i == X-1:
                T += 0
            elif i >= X:
                T += D
        print(T)
