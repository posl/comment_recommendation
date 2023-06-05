def distance(x,y):
    d = 0
    for i in range(len(x)):
        d += (x[i]-y[i])**2
    return d**0.5
N,D = map(int,input().split())
X = []
for i in range(N):
    X.append(list(map(int,input().split())))
ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        if distance(X[i],X[j]).is_integer():
            ans += 1
print(ans)

if __name__ == '__main__':
    distance()