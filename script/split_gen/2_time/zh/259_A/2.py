def main():
    N,M,X,T,D = map(int,input().split())
    if M == 0:
        print(T)
        return
    if M == X:
        print(T)
        return
    if M == N:
        print(T + (N-X)*D)
        return
    if X > M:
        print(T + (X-M)*D)
        return
    if X < M:
        print(T + (M-X)*D)
        return
