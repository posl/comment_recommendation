def main():
    A,B,X = map(int,input().split())
    #print(A,B,X)
    N = 0
    for i in range(1,10):
        if X >= A * (10**i) + B * (i+1):
            N = 10**i
        else:
            break
    #print(N)
    if N == 0:
        print(0)
        return
    for j in range(1,N+1):
        if X >= A * (N-j) + B * (len(str(N-j))+1):
            print(N-j)
            return
