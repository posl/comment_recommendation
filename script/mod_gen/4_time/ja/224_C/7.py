def area(x1,y1,x2,y2,x3,y3):
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2
N=int(input())
X=[]
Y=[]
for i in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
ans=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if area(X[i],Y[i],X[j],Y[j],X[k],Y[k])>0:
                ans+=1
print(ans)

if __name__ == '__main__':
    area()