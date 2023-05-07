def main():
    N,X = map(int,input().split())
    x = list(map(int,input().split()))
    #print(N,X,x)
    #print(abs(X-x[0]))
    d = abs(X-x[0])
    for i in range(N):
        d = gcd(d,abs(X-x[i]))
    print(d)
