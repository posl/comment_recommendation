def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
N,X = map(int,input().split())
Xs = list(map(int,input().split()))
Xs.append(X)
Xs.sort()
D = Xs[1]-Xs[0]
for i in range(1,N):
    D = gcd(D,Xs[i+1]-Xs[i])
print(D)
I'm not sure if this is the most efficient way to do this, but it works.
