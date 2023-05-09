def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    Y = []
    for i in range(M):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    time = T
    room = 0
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print('No')
            break
        else:
            room += 1
            if room in X:
                time += Y[X.index(room)]
    if time > 0:
        print('Yes')
